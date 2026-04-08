#!/usr/bin/env python3
"""Configuration management for kslearn CLI"""

import os
import json
from pathlib import Path
from typing import Optional, Dict

# Config locations — use centralized loader paths
from kslearn.loader import CONFIG_DIR
CONFIG_LOCATIONS = [
    CONFIG_DIR / "settings.json",
    Path.home() / ".kslearnrc",
    Path.home() / ".kslearn" / "config.json",
    Path.cwd() / ".kslearnrc",
    Path.cwd() / "kslearn.json",
]

DEFAULT_CONFIG = {
    "theme": "sky_blue",
    "sound": False,
    "auto_timer": True,
    "timer_minutes": 3,
    "show_explanations": True,
    "difficulty": "mixed",
    "language": "en",
    "username": "",
    "api_key": "",
    # Learning-focused settings
    "daily_goal_minutes": 30,
    "focus_track": "general",
    "notification_enabled": True,
    # API provider settings
    "api_provider": "anthropic",
    # UI preferences
    "use_rich_ui": True,
    "color_scheme": "cyan",
    # Progress tracking
    "bookmarks": [],
    "learning_progress": {},
    # Study streak tracking
    "study_streak": {
        "current": 0,
        "best": 0,
        "last_study_date": None,
    },
    # Achievements
    "achievements": [],
    # Spaced repetition
    "review_queue": {},
    # Daily goal tracking
    "daily_goal": {
        "today_date": None,
        "minutes_studied": 0,
    },
    # Multi-user profiles
    "active_profile": "default",
    "profiles": {
        "default": {
            "name": "Default User",
            "created": None,
        }
    },
    # User preferences
    "flashcard_mode": False,
    "timed_quiz_best": 0,
    "tutorial_progress": {},
}


def find_config() -> Optional[Path]:
    """Find existing config file"""
    for loc in CONFIG_LOCATIONS:
        if loc.exists():
            return loc
    return None


def load_config() -> dict:
    """Load configuration from file, merging profile-scoped data for the active profile."""
    config_path = find_config()
    if config_path:
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                user_config = json.load(f)
                config = {**DEFAULT_CONFIG, **user_config}

                # Merge profile-scoped data into root keys
                profile_name = config.get("active_profile", "default")
                for key in _PROFILE_KEYS:
                    data_key = _get_profile_data_key(profile_name, key)
                    if data_key in config:
                        config[key] = config[data_key]

                # Strip stale root-level profile keys so they don't leak back
                # on next save. Profile data is authoritative.
                for key in _PROFILE_KEYS:
                    if key in user_config:
                        del config[key]
                        # Also delete from original user_config to prevent re-write
                        # (we only delete from merged config; file stays as-is)

                return config
        except (json.JSONDecodeError, IOError):
            pass

    # Auto-migrate on first load
    return DEFAULT_CONFIG.copy()


def save_config(config: dict, path: Optional[Path] = None) -> Path:
    """Save configuration to file, writing profile-scoped data to correct keys."""
    if path is None:
        path = CONFIG_DIR / "settings.json"

    # Ensure parent directory exists
    path.parent.mkdir(parents=True, exist_ok=True)

    # Write profile-scoped data back to profile keys before saving
    profile_name = config.get("active_profile", "default")
    for key in _PROFILE_KEYS:
        data_key = _get_profile_data_key(profile_name, key)
        if key in config:
            config[data_key] = config[key]

    with open(path, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2, ensure_ascii=False)

    return path


def init_config() -> dict:
    """Initialize config with defaults if not exists"""
    config_path = find_config()
    if config_path:
        config = load_config()

        # Migrate existing root data to default profile
        profile_name = config.get("active_profile", "default")
        migration_key = f"profile_{profile_name}_migrated"
        if not config.get(migration_key):
            for key in _PROFILE_KEYS:
                if key in config:
                    data_key = _get_profile_data_key(profile_name, key)
                    if data_key not in config:
                        config[data_key] = config[key]
            config[migration_key] = True
            save_config(config)

        return config

    # Create default config in home directory
    config = DEFAULT_CONFIG.copy()
    save_config(config)
    return config


def get_config_value(key: str, default=None):
    """Get a specific config value"""
    config = load_config()
    return config.get(key, default)


def set_config_value(key: str, value):
    """Set a specific config value and save"""
    config = load_config()
    config[key] = value
    save_config(config)
    return config


def reset_config() -> dict:
    """Reset config to defaults"""
    config_path = find_config()
    if config_path:
        config_path.unlink()
    return DEFAULT_CONFIG.copy()


# --- Study Streak Tracking ---

def update_study_streak():
    """Update the study streak counter. Call this whenever user studies."""
    from datetime import datetime, timedelta

    config = load_config()
    profile_name = config.get("active_profile", "default")

    # Use profile-scoped key
    streak_key = _get_profile_data_key(profile_name, "study_streak")
    streak = config.get(streak_key, {"current": 0, "best": 0, "last_study_date": None})
    today = datetime.now().strftime("%Y-%m-%d")
    yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    last_date = streak.get("last_study_date")

    if last_date == today:
        return streak  # Already studied today

    if last_date == yesterday or last_date is None:
        streak["current"] = streak.get("current", 0) + 1
    else:
        streak["current"] = 1  # Streak broken, reset

    streak["best"] = max(streak.get("best", 0), streak["current"])
    streak["last_study_date"] = today

    config[streak_key] = streak
    save_config(config)
    return streak


# --- Daily Goal Tracking ---

def update_daily_goal(minutes: int = 5):
    """Add minutes to today's study goal."""
    from datetime import datetime

    config = load_config()
    profile_name = config.get("active_profile", "default")
    today = datetime.now().strftime("%Y-%m-%d")

    goal_key = _get_profile_data_key(profile_name, "daily_goal")
    goal = config.get(goal_key, {"today_date": None, "minutes_studied": 0})

    if goal.get("today_date") != today:
        goal = {"today_date": today, "minutes_studied": 0}

    goal["minutes_studied"] = goal.get("minutes_studied", 0) + minutes
    config[goal_key] = goal
    save_config(config)
    return goal


def get_daily_goal_progress():
    """Get today's goal progress."""
    from datetime import datetime

    config = load_config()
    profile_name = config.get("active_profile", "default")
    today = datetime.now().strftime("%Y-%m-%d")
    goal_minutes = config.get("daily_goal_minutes", 30)

    goal_key = _get_profile_data_key(profile_name, "daily_goal")
    daily = config.get(goal_key, {})

    if daily.get("today_date") != today:
        return {"minutes": 0, "goal": goal_minutes, "percentage": 0}

    minutes = daily.get("minutes_studied", 0)
    return {
        "minutes": minutes,
        "goal": goal_minutes,
        "percentage": min((minutes / goal_minutes) * 100, 100) if goal_minutes > 0 else 0,
    }


# --- Multi-User Profiles ---
# Profile-scoped data keys: learning_progress, bookmarks, achievements,
# study_streak, daily_goal, review_queue, tutorial_progress, timed_quiz_best

_PROFILE_KEYS = [
    "learning_progress", "bookmarks", "achievements",
    "study_streak", "daily_goal", "review_queue",
    "tutorial_progress", "timed_quiz_best", "verse_progress",
]


def _get_profile_data_key(profile_name: str, key: str) -> str:
    """Get the config key for profile-specific data."""
    return f"profile_{profile_name}_{key}"


def get_active_profile():
    """Get the active user profile."""
    config = load_config()
    profile_name = config.get("active_profile", "default")
    profiles = config.get("profiles", {})
    return profiles.get(profile_name, {"name": "Default User"})


def get_active_profile_name():
    """Get the active profile name string."""
    config = load_config()
    return config.get("active_profile", "default")


def list_profiles():
    """List all user profiles."""
    config = load_config()
    return config.get("profiles", {})


def create_profile(name: str, display_name: str) -> Dict:
    """Create a new user profile."""
    from datetime import datetime

    config = load_config()
    profiles = config.get("profiles", {})

    if name in profiles:
        return None  # Already exists

    profiles[name] = {
        "name": display_name,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    config["profiles"] = profiles
    save_config(config)
    return profiles[name]


def switch_profile(name: str) -> bool:
    """Switch to a different user profile."""
    config = load_config()
    profiles = config.get("profiles", {})

    if name not in profiles:
        return False

    config["active_profile"] = name
    save_config(config)
    return True


def get_profile_value(profile_name: str, key: str, default=None):
    """Get a profile-scoped value from config."""
    config = load_config()
    data_key = _get_profile_data_key(profile_name, key)
    return config.get(data_key, config.get(key, default))


def set_profile_value(profile_name: str, key: str, value):
    """Set a profile-scoped value in config."""
    config = load_config()
    data_key = _get_profile_data_key(profile_name, key)
    config[data_key] = value
    save_config(config)


def migrate_to_profiles():
    """Migrate root-level data to the default profile if not already done."""
    config = load_config()
    profile_name = "default"

    # Check if migration already done
    migration_key = f"profile_{profile_name}_migrated"
    if config.get(migration_key):
        return

    # Migrate each profile-scoped key
    for key in _PROFILE_KEYS:
        if key in config:
            data_key = _get_profile_data_key(profile_name, key)
            config[data_key] = config[key]

    config[migration_key] = True
    save_config(config)


def get_profiled_config():
    """Get config with profile-scoped data resolved.
    Returns a merged config where profile keys override root keys."""
    config = load_config()
    profile_name = config.get("active_profile", "default")

    merged = config.copy()
    for key in _PROFILE_KEYS:
        data_key = _get_profile_data_key(profile_name, key)
        if data_key in config:
            merged[key] = config[data_key]
        elif key not in merged:
            # Apply defaults
            if key == "study_streak":
                merged[key] = {"current": 0, "best": 0, "last_study_date": None}
            elif key == "daily_goal":
                merged[key] = {"today_date": None, "minutes_studied": 0}
            elif key == "review_queue":
                merged[key] = {}
            elif key in ("learning_progress", "bookmarks", "achievements", "tutorial_progress"):
                merged[key] = {} if key != "bookmarks" else []
            elif key == "timed_quiz_best":
                merged[key] = 0
            elif key == "verse_progress":
                merged[key] = {
                    "total_xp": 0,
                    "worlds": {},
                    "achievements": [],
                    "combo_multiplier": 1.0,
                    "combo_count": 0,
                    "difficulty": "normal",
                    "compact_mode": False,
                    "animate_narrative": False,
                    "lifelines": {"fifty_fifty": 3, "skip": 2, "hint": 3},
                    "inventory": [],
                    "weaknesses": {},
                    "lore_unlocked": [],
                    "speedrun_records": {},
                    "daily_challenge": None,
                    "npc_memory": {},
                    "secrets_found": [],
                    "session_stats": {"total_sessions": 0, "total_time": 0, "total_correct": 0, "total_wrong": 0, "history": []},
                    "streak_calendar": {},
                    "prestige_level": 0,
                    "prestige_bonus": 0,
                    "custom_questions": [],
                    "mentor_active": False,
                    "world_themes": {},
                    "quote_index": 0,
                    "journal": {},
                    "sound_enabled": True,
                    "daily_challenge_best": 0,
                }

    return merged
