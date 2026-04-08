# 🌌 KSL-Verse — Complete Game Design Document

> **An Interactive Multiverse Learning Experience for KSLearn**
> Version 2.0 — April 2026

---

## 📖 Overview

**KSL-Verse** is a story-driven, choice-based educational game embedded within the KSLearn CLI. Players explore themed "worlds" — each representing a subject domain — progressing through levels filled with narrative scenarios, interactive choices, XP rewards, and epic boss battles.

**Completely self-contained** — no dependency on quiz files or other KSLearn engines. All content lives in `*_verse.json` files.

---

## 🎮 Core Concept

### The Premise
You are a **Verse Walker** — a learner who can traverse between knowledge universes. Each universe contains multiple worlds, and each world is divided into levels you must conquer by answering questions, making choices, and proving your mastery.

### Gameplay Loop
```
Select World → View Level Map → Enter Level → Read Scenario Narrative
  → Make Choices (A/B/C/D) → Earn XP → Unlock Next Scenario
    → Complete All Scenarios → Face Boss Battle → Conquer World!
```

### Key Mechanics

| Mechanic | Description |
|----------|-------------|
| **XP (Experience Points)** | Earned per correct answer. Streaks multiply rewards. |
| **Player Level** | Total XP determines your Verse Walker rank. Higher levels unlock prestige. |
| **Worlds** | Themed knowledge domains (e.g., WebDev Cosmos). Content in `*_verse.json`. |
| **Levels** | Progressive stages within a world. Each has a story arc. |
| **Scenarios** | Narrative-driven nodes with a story beat + multiple-choice question. |
| **Branching Outcomes** | Correct answers advance the story; wrong answers trigger explanations and retries. |
| **Boss Battles** | Final challenge of each world — harder, multi-part questions with bonus XP. |
| **Achievements** | Special badges for milestones (first world, speed runs, perfect scores, etc.). |

---

## 🗺️ World Structure

Each world is defined in a `*_verse.json` file:

```json
{
  "verse": {
    "id": "webdev_cosmos",
    "title": "WebDev Cosmos",
    "description": "From markup to mastery...",
    "icon": "🌐",
    "difficulty": "beginner",
    "player_level_required": 1,
    "lore": { "origin_of_cosmos": { "title": "...", "icon": "🌌", "content": "..." } },
    "side_quests": [
      { "id": "sq_1", "name": "Speed Demon", "description": "Complete a level in under 60s",
        "requirements": { "levels_completed": 1 }, "xp_reward": 100 }
    ],
    "levels": [
      {
        "id": "level_1",
        "title": "The HTML Highlands",
        "story_intro": "You materialize on a plateau...",
        "icon": "🏔️",
        "xp_reward_per_scenario": 25,
        "concepts": ["DOCTYPE", "Semantic HTML", "Forms"],
        "scenarios": [
          {
            "id": "scene_1",
            "concept": "DOCTYPE",
            "narrative": "The Builder approaches...",
            "question": "Which line declares the document type?",
            "options": [
              {"letter": "A", "text": "<!DOCTYPE html>", "correct": true},
              {"letter": "B", "text": "<html>", "correct": false}
            ],
            "explanation_correct": "<!DOCTYPE html> tells the browser...",
            "explanation_wrong": "HTML5 uses <!DOCTYPE html>...",
            "related_concepts": ["HTML5", "Browser Rendering"],
            "is_secret": true,
            "secret_lore_id": "origin_of_cosmos",
            "secret_lore_title": "The Origin of the WebDev Cosmos",
            "secret_lore_content": "In the beginning..."
          }
        ],
        "mini_boss": {
          "name": "The Tag Gatekeeper", "xp_reward": 75,
          "questions": [ {...} ]
        },
        "boss": {
          "name": "The Markup Sentinel",
          "narrative": "A towering figure blocks your path...",
          "xp_reward": 150,
          "questions": [ {...} ]
        }
      }
    ],
    "epilogue": "The WebDev Cosmos trembles..."
  }
}
```

---

## 🌐 WebDev Cosmos — Starter World

> *"From markup to mastery — forge your path through the fabric of the web."*

| Level | Name | Theme | Icon |
|-------|------|-------|------|
| 1 | The HTML Highlands | HTML fundamentals — structure, semantic tags, forms | 🏔️ |
| 2 | The CSS Canyons | CSS — selectors, box model, flexbox, colors | 🎨 |
| 3 | The JavaScript Junction | JS basics — variables, functions, conditionals | ⚡ |
| 4 | The DOM Delta | DOM manipulation, events, event bubbling | 🌊 |
| 5 | The Async Abyss | Callbacks, Promises, async/await, fetch API | 🔮 |

Each level has **5 scenarios** + **1 mini-boss** (mid-level) + **1 boss battle** (end of world).

---

## 🏆 XP & Player Level System

### XP Rewards
| Action | XP |
|--------|----|
| Correct scenario answer | 25 XP |
| Correct boss question | 30 XP |
| Scenario streak (3+ correct) | +5 bonus per streak |
| Perfect level (no wrong answers) | +50 bonus |
| Perfect world (all levels perfect) | +200 bonus |
| First world completion | +100 bonus |

### Player Levels (Verse Walker Ranks)

| Level | Rank Title | Total XP Required |
|-------|-----------|-------------------|
| 1 | Novice Walker | 0 |
| 2 | Apprentice Explorer | 200 |
| 3 | Seasoned Voyager | 500 |
| 4 | Knowledge Seeker | 1,000 |
| 5 | Realm Wanderer | 2,000 |
| 6 | Domain Master | 3,500 |
| 7 | Cosmos Sage | 5,500 |
| 8 | Universe Architect | 8,000 |
| 9 | Multiverse Legend | 12,000 |
| 10 | Verse Transcendent | 20,000 |

---

## 🎮 Game Modes

| Mode | Description |
|------|-------------|
| **Story Mode** | Relaxed pace, hints available, forgiving wrong answers |
| **Normal** | Standard experience |
| **Hard Mode** | 1.5x XP, no hints, no forgiveness |
| **Ironman** | 2x XP, one wrong answer = run ends |
| **Marathon** | 3x XP, complete entire world back-to-back |
| **Boss Rush** | Fight all world bosses in sequence |
| **Endless** | Infinite random scenarios — one wrong = game over |
| **Survival** | 3 lives — wrong answers cost lives |
| **Randomizer** | 10 random scenarios from all worlds |
| **Practice** | No penalties, no XP — just learning |

---

## 🧩 Additional Features

### Side Quests
Optional challenges per world defined in verse JSON. Examples:
- "Answer 5 code questions in a row for 100 bonus XP"
- "Complete a level without using lifelines"
- "Get 100% on the boss battle"

### Lifelines (3 Types)
- **50/50** — Remove 2 wrong options (3 uses, resettable)
- **Skip** — Bypass a scenario (2 uses)
- **Hint** — Get a clue about the answer (3 uses)

### Items / Inventory
Random drops (10% chance per correct answer):
| Item | Effect |
|------|--------|
| 🔮 Syntax Shard | +1 hint use |
| 💎 Logic Gem | +2 hint uses |
| 🔥 Streak Crystal | 1.5x XP for next level |
| 📜 Lore Scroll | Unlock a lore entry |
| ⏭️ Skip Token | Skip next scenario |
| 🛡️ Shield Charm | Absorb one wrong answer penalty |
| 🔵 Memory Orb | Boost spaced review priority |
| 🧪 XP Potion | Instant 50 XP |
| 🧭 Compass | Show weakest area |

### Difficulty Scaling
Questions auto-adjust difficulty based on player accuracy. Hard questions appear more often for strong areas, easy questions for weak areas.

### NPC System
Each world has themed NPCs who:
- Greet you differently based on visit count and progress
- Give personalized farewell messages based on performance
- Provide mentor advice about your weakest areas
- Challenge you as a Rival Walker at milestones (3 questions, 100 XP)

### World Lore Codex
Collectible lore entries unlocked by discovering hidden secrets (5% chance per scenario). Each world has its own lore with backstory, developer quotes, and Easter eggs.

### Boss Phases
Boss battles split into **Phase 1** (first half) and **Phase 2** (second half). If struggling in Phase 1, Phase 2 questions get harder with visual "BOSS ENRAGED" notification.

### Seasonal Events
Limited-time bonuses:
- **Code Week** (May 1-7): Double XP
- **Hacktober** (October): 1.5x XP, spooky-themed challenges

### Prestige System
After reaching max level (20,000 XP), reset progress for:
- Permanent +10% XP bonus per prestige level
- Exclusive prestige titles (Prestige I–X, Ascendant, Eternal)
- Keeps lore, journal entries, and custom questions

### Mid-World Checkpoints
Save progress mid-level so you don't lose everything on quit. Resume prompt appears when re-entering a world.

### Custom Questions
Players can author and inject their own questions into any world level. Questions appear randomly during gameplay (30% chance).

### World Builder (In-App)
Guided CLI wizard to create new verse worlds — no JSON editing required. Prompts for world info, scenarios, and boss questions, then generates `*_verse.json`.

### AI World Generator (from Course Catalog)
The primary world creation method. Uses **tgpt/sky** AI with `ThreadPoolExecutor` for parallel generation:

1. **Browse Course Catalog** — Shows all existing hierarchical courses from `data/ksl/`
2. **Pick a Course** — Select any course as source material
3. **AI generates in parallel** (up to 10 workers):
   - Each course category → a game level with 5 story-driven scenarios
   - Mini-boss per level
   - Final boss battle covering all course concepts
   - Lore entries inspired by course content
   - Cinematic epilogue
4. **Fallback option** — If no courses exist, create a custom world manually

The AI transforms educational course content (categories, units, outcomes, subtopics) into immersive adventure game scenarios while preserving the learning objectives. No quiz files are used — pure course catalog → verse world conversion.

---

## 📊 Analytics & Export

| Feature | Description |
|---------|-------------|
| **Deep Stats** | Total sessions, time, accuracy trends, improvement graphs |
| **Streak Calendar** | 30-day heatmap of verse study days |
| **Performance Timeline** | Score trends over time with 📈/📉 icons |
| **Weakness Tracker** | Spaced review scheduling for wrong answers |
| **Import/Export** | Backup and restore progress via JSON file |
| **Share Codes** | Generate a hash code from your stats to share |
| **Report Card** | Semester-style grade (A+ to F) with world breakdown |
| **Profile Card** | Copyable ASCII card with your stats |

---

## 🏅 Achievements (32 Total)

### Original (15)
First Steps, Quiz Master, Perfectionist, Hot Streak, Month Warrior, Knowledge Seeker, Walking Encyclopedia, Explorer, Speed Demon, Bookworm, Flash of Genius, Consistent Learner, Renaissance Mind, Tutorial Graduate, Profile Creator

### KSL-Verse (17)
First Steps in the Verse, Level Cleared, World Conqueror, Perfect Run, Streak Walker, Boss Slayer, Multiverse Explorer, Verse Transcendent, Secret Hunter, Daily Champion, Speed Runner, Combo Master, Masochist (Hard Mode), Collector, Lore Master, Reborn (Prestige), Journaler, Iron Will, Marathon Runner, Question Author

---

## 🎭 Accessibility Options

- **High Contrast Mode** — Bolder colors, clearer separators
- **Large Text Mode** — Bigger fonts throughout
- **Reduced Motion** — No typing animations
- **Sound Effects Toggle** — Terminal bell on/off
- **Compact Mode** — Questions only, minimal narrative

---

## 📝 JSON Schema Reference

### Verse File
| Key | Type | Required |
|-----|------|----------|
| `verse.id` | string | ✅ |
| `verse.title` | string | ✅ |
| `verse.description` | string | ✅ |
| `verse.icon` | emoji | ✅ |
| `verse.difficulty` | string | ✅ |
| `verse.player_level_required` | number | ✅ |
| `verse.lore` | object | ❌ |
| `verse.side_quests` | array | ❌ |
| `verse.epilogue` | string | ❌ |
| `verse.levels` | array | ✅ |

### Level
| Key | Type | Required |
|-----|------|----------|
| `level.id` | string | ✅ |
| `level.title` | string | ✅ |
| `level.story_intro` | string | ✅ |
| `level.icon` | emoji | ✅ |
| `level.xp_reward_per_scenario` | number | ✅ |
| `level.concepts` | array | ❌ |
| `level.scenarios` | array | ✅ |
| `level.mini_boss` | object | ❌ |
| `level.boss` | object | ❌ |

### Scenario
| Key | Type | Required |
|-----|------|----------|
| `scenario.id` | string | ✅ |
| `scenario.concept` | string | ❌ |
| `scenario.narrative` | string | ✅ |
| `scenario.question` | string | ✅ |
| `scenario.options` | array | ✅ |
| `scenario.explanation_correct` | string | ✅ |
| `scenario.explanation_wrong` | string | ✅ |
| `scenario.related_concepts` | array | ❌ |
| `scenario.is_secret` | boolean | ❌ |
| `scenario.secret_lore_id` | string | ❌ |
| `scenario.code` | string | ❌ (for code output questions) |

---

## 🔧 Technical Implementation

### Files
| File | Purpose |
|------|---------|
| `kslearn/engines/verse_engine.py` | Core game engine (~3,400 lines) |
| `data/ksl/webdev_verse.json` | WebDev Cosmos world content |
| `data/ksl/*_verse.json` | Custom/generated worlds |
| `docs/KSL_VERSE_GAME_DESIGN.md` | This document |

### Modified Files
| File | Changes |
|------|---------|
| `kslearn/config.py` | Added `verse_progress` profile key + defaults |
| `kslearn/engines/achievements.py` | Added 17 verse achievements |
| `kslearn/cli.py` | Added option 9/V/VERSE to main menu + `kslearn verse` command |

### Content Loading
- Discovers all `*_verse.json` files in `data/ksl/`
- No dependency on quiz engine or `.ksl` files
- Worlds auto-discovered on menu load
- Custom worlds added via World Builder or manual JSON

### State Persistence
All progress stored in `settings.json` under `verse_progress`:
```json
{
  "verse_progress": {
    "total_xp": 0,
    "worlds": {},
    "combo_multiplier": 1.0,
    "difficulty": "normal",
    "lifelines": {"fifty_fifty": 3, "skip": 2, "hint": 3},
    "inventory": [],
    "weaknesses": {},
    "lore_unlocked": [],
    "speedrun_records": {},
    "session_stats": {...},
    "streak_calendar": {},
    "prestige_level": 0,
    "journal": {},
    "sound_enabled": true
  }
}
```

---

## 🚀 Future Expansion

### New Worlds (Planned)
- 🐍 **Python Kingdom** — Python fundamentals
- 🗄️ **Data Dimension** — SQL, databases
- 🧬 **Science Galaxy** — Physics, chemistry, biology
- 📜 **History Timeline** — Historical events
- 🔢 **Math Universe** — Algebra, statistics

### Planned Features
- 🎵 Background chiptune music
- 🏅 Online leaderboards
- 📖 World lore encyclopedia (searchable)
- 🔄 Daily verse challenges (rotating scenario sets)
- 🎨 Custom player avatars
- 📱 Mobile app companion

---

## 📝 Version History

| Version | Date | Notes |
|---------|------|-------|
| 1.0 | April 2026 | Initial release — WebDev Cosmos, XP system, achievements |
| 2.0 | April 2026 | Added: Boss Rush, Endless, Survival, Randomizer, Side Quests, Difficulty Scaling, Unlock Cinematics, Secret Worlds, Rival NPC, Seasonal Events, Checkpoints, Resume Prompt, Import/Export, Share Codes, Report Card, World Builder, Auto-Generate, Accessibility, Deep Stats, Streak Calendar, Performance Timeline, Mastery Levels, Custom Questions, Terminal Sound Effects |

---

*Designed for KSLearn — Making learning an adventure.*
