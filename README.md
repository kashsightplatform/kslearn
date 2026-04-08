<p align="center">
  <img src="https://github.com/kashsightplatform/kslearn/blob/main/screenshots/banner.png" alt="kslearn Banner" width="600" />
</p>

<h1 align="center">kslearn</h1>

<p align="center">
  <strong>Learn anything — by studying, not just memorizing.</strong>
</p>

<p align="center">
  <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/python-3.7+-blue.svg" alt="Python 3.7+" /></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-Proprietary-red.svg" alt="License: Proprietary" /></a>
  <a href="https://termux.dev/"><img src="https://img.shields.io/badge/Termux-✓-green.svg" alt="Termux Compatible" /></a>
  <a href="https://github.com/kashsightplatform/kslearn"><img src="https://img.shields.io/badge/version-2.0.0-cyan.svg" alt="Version 2.0.0" /></a>
</p>

---

## ✨ What is kslearn?

kslearn is an **offline-first educational learning system** that combines comprehensive study notes, interactive quizzes, flashcards, step-by-step tutorials, hierarchical courses with progression gating, AI chat with proactive suggestions, and **KSL-Verse** — a full RPG-style multiverse learning game — all in one terminal app.

**No internet required.** Everything works locally. Only the AI Chat feature may need a connection (or use the built-in offline mode).

<p align="center">
  <img src="https://github.com/kashsightplatform/kslearn/blob/main/screenshots/main_menu.png" alt="Main Menu" width="500" />
</p>

---

## 🚀 Features

### 📚 Core Learning

| Feature | Description |
|---------|-------------|
| 📂 **Course Catalog** | 6-level hierarchical courses with progression gating, AI tutor |
| 📚 **Study Notes** | 50+ topics across multiple subjects with reading time tracking |
| 📝 **Quizzes** | Multiple-choice with explanations, timed mode, assessments |
| 🤖 **AI Chat** | 11 AI providers (5 free) with proactive "What to Study Next" suggestions |
| 📊 **My Progress** | Analytics dashboard, quiz scores, achievements, export report |
| 🔖 **Study Tools** | Bookmarks, global search, spaced review |
| 🧠 **Knowledge Brain** | Offline Q&A database with auto-save from AI chat |
| 🏪 **Data Store** | Download free & premium content |
| 👤 **Profiles** | Multiple users, separate progress, profile-scoped data |
| ⚙️ **Settings** | Theme, daily goal, API provider, spaced review limit |

### 🌌 KSL-Verse — Multiverse Learning Game

**A full RPG-style game where learning is an adventure:**

#### Game Modes
| Mode | Description |
|------|-------------|
| ⚔️ **Story Mode** | Relaxed pace, hints available |
| ⚔️ **Normal** | Standard experience |
| 🔥 **Hard Mode** | 1.5x XP, no hints |
| 💀 **Ironman** | One wrong = run ends, 2x XP |
| 🏃 **Marathon** | Full world back-to-back, 3x XP |
| ⚔️ **Boss Rush** | Fight all bosses in sequence |
| ♾️ **Endless** | Infinite scenarios — one wrong = game over |
| 💀 **Survival** | 3 lives — wrong answers cost lives |
| 🎲 **Randomizer** | 10 random shuffled scenarios |
| 🏃 **Practice** | No penalties — just learning |

#### Game Features
- **5 levels** with story-driven scenarios per world
- **Mini-bosses** mid-level + **Boss battles** at world end (with Phase 2)
- **XP system** with combo multipliers and prestige
- **Lifelines**: 50/50, Skip, Hint
- **Items & Inventory**: Drops from correct answers
- **NPCs** with memory, mentor advice, rival challenges
- **Lore Codex**: Discover hidden secrets and world backstory
- **World Builder**: Create worlds via CLI wizard
- **AI World Generator**: Pull from Course Catalog → parallel AI generates full worlds
- **Import/Export**: Backup and restore progress
- **Share Codes**: Compare with friends
- **Accessibility**: High contrast, large text, reduced motion

#### Player Progression
| Level | Rank | XP Required |
|-------|------|-------------|
| 1 | Novice Walker | 0 |
| 2 | Apprentice Explorer | 200 |
| 3 | Seasoned Voyager | 500 |
| 5 | Realm Wanderer | 2,000 |
| 7 | Cosmos Sage | 5,500 |
| 10 | Verse Transcendent | 20,000 |

**32 achievements** across 4 rarity tiers. **Prestige system** for endgame replay value.

### 🔥 AI-Powered Addictive Suggestions

Every interaction proactively suggests what to learn next — after chat, quizzes, courses, searches, and streak milestones.

---

## 📋 Main Menu

| # | Option | Shortcut | Description |
|---|--------|----------|-------------|
| 1 | 📂 Course Catalog | `1` / `CC` | Hierarchical courses with AI tutor |
| 2 | 📚 Study Notes | `2` / `N` | Browse learning materials |
| 3 | 📝 Take Quiz | `3` / `Q` | Test your knowledge |
| 4 | 🤖 AI Chat | `4` | AI tutor (online & offline) |
| 5 | 📊 My Progress | `5` / `P` | Analytics, achievements, export |
| 6 | 🔖 Study Tools | `6` / `T` | Bookmarks, search, spaced review |
| 7 | 🧠 Knowledge Brain | `7` / `B` | Offline Q&A database |
| 8 | 🏪 Data Store | `8` | Download content |
| 9 | 🌌 KSL-Verse | `9` / `V` | **Multiverse learning game** |
| S | ❤️ Support | `S` | Credits, email, website |
| F | 🎮 Study Modes | `F` / `M` | Flashcards, timed quiz, tutorials |
| D | 👤 Profiles | `D` | Switch or manage profiles |
| C | ⚙️ Settings | `C` | Configure experience |
| H | ❓ Help | `H` | Usage info |
| 0 | ❌ Exit | `0` | Leave kslearn |

---

## 📦 Quick Start

```bash
# Install
pip install -e .

# Launch
kslearn

# Launch KSL-Verse directly
kslearn verse
```

---

## 📥 Installation

### Prerequisites

- Python 3.7+
- `rich` library for terminal UI
- `click` library for CLI framework

### From Source

```bash
# Clone
git clone https://github.com/kashsightplatform/kslearn.git
cd kslearn

# Install dependencies
pip install rich click

# Install in editable mode
pip install -e .

# Run
kslearn
```

### On Termux (Android)

```bash
pkg install python
pip install rich click
git clone https://github.com/kashsightplatform/kslearn.git
cd kslearn
pip install -e .
kslearn
```

---

## 🌌 KSL-Verse Deep Dive

### World Structure

Each world is a `*_verse.json` file in `data/ksl/`:

```
WebDev Cosmos 🌐
├── Level 1: The HTML Highlands 🏔️ (5 scenarios + mini-boss)
├── Level 2: The CSS Canyons 🎨 (5 scenarios + mini-boss)
├── Level 3: The JavaScript Junction ⚡ (5 scenarios + mini-boss)
├── Level 4: The DOM Delta 🌊 (5 scenarios + mini-boss)
├── Level 5: The Async Abyss 🔮 (5 scenarios + mini-boss)
└── Boss: The Chrono Phantom ⚔️ (5 questions, 150 XP)
```

### AI World Generator

```
Course Catalog → Select Course → AI Generates in Parallel → Playable World
```

Uses **tgpt/sky** with `ThreadPoolExecutor` for parallel generation:
- Each course category → a game level
- 5 scenarios per level + mini-boss
- Boss battle covering all concepts
- Lore entries + epilogue
- Falls back gracefully if AI fails

### Content Format

All verse content is plain JSON — no encryption, no packaging:

```json
{
  "verse": {
    "id": "my_world",
    "title": "My World",
    "icon": "🌍",
    "difficulty": "beginner",
    "levels": [
      {
        "id": "level_1",
        "title": "First Steps",
        "scenarios": [...],
        "boss": {...}
      }
    ]
  }
}
```

---

## 📁 Project Structure

```
kslearn/
├── kslearn/
│   ├── cli.py                    # Main CLI entry point
│   ├── config.py                 # Configuration management
│   ├── ui.py                     # Rich UI components with theming
│   ├── loader.py                 # Content loader (.ksl + JSON)
│   ├── ksl_loader.py             # KSL file parser
│   ├── protector.py              # Content encryption/signing
│   ├── engines/
│   │   ├── quiz_engine.py        # Quiz system
│   │   ├── notes_viewer.py       # Notes + hierarchical courses
│   │   ├── tutorials.py          # Tutorial engine
│   │   ├── achievements.py       # Badge system (32 achievements)
│   │   └── verse_engine.py       # KSL-Verse game engine (~3,900 lines)
│   └── main/
│       ├── ai_chat.py            # AI tutor with suggestions
│       ├── datastore.py          # Content store
│       └── support.py            # Social links
├── data/
│   ├── ksl/                      # Content packages
│   └── config/settings.json      # User settings
├── docs/                         # Documentation
└── website/                      # Firebase-hosted website
```

---

## 🔧 Content Tool

Build encrypted `.ksl` packages:

```bash
python ksl_tool.py build data/my_subject.json -o data/my_subject.ksl
python ksl_tool.py verify data/my_subject.ksl
python ksl_tool.py info data/my_subject.ksl
```

---

## 🌐 Website

Visit **[kash-sight.web.app](https://kash-sight.web.app)** for:

- Project showcase
- KSL Store (free & premium content)
- LearnQuest (quiz-to-reward system)
- Blog & contact form

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch
3. Add content as `.json` files in `data/ksl/`
4. Submit a pull request

---

## 📄 License

Proprietary — KashSight Platform

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/kashsightplatform">KashSight</a>
</p>
