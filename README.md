<p align="center">
  <img src="https://github.com/kashsightplatform/kslearn/blob/main/screenshots/banner.png" alt="kslearn Banner" width="600" />
</p>

<h1 align="center">kslearn</h1>

<p align="center">
  <strong>Learn anything — by studying, not just memorizing.</strong>
</p>

<p align="center">
  <a href="https://www.python.org/downloads/">
    <img src="https://img.shields.io/badge/python-3.7+-blue.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.7+" />
  </a>
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/License-Proprietary-red.svg?style=for-the-badge" alt="License" />
  </a>
  <a href="https://termux.dev/">
    <img src="https://img.shields.io/badge/Termux-✓-green.svg?style=for-the-badge&logo=termux&logoColor=white" alt="Termux Compatible" />
  </a>
  <a href="https://github.com/kashsightplatform/kslearn">
    <img src="https://img.shields.io/badge/version-2.0.0-cyan.svg?style=for-the-badge" alt="Version 2.0.0" />
  </a>
  <a href="https://github.com/kashsightplatform/kslearn/stargazers">
    <img src="https://img.shields.io/badge/Stars-100+-yellow.svg?style=for-the-badge&logo=github&logoColor=white" alt="Stars" />
  </a>
</p>

<p align="center">
  <a href="#-features">Features</a> •
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-installation">Installation</a> •
  <a href="#-ksl-verse">KSL-Verse</a> •
  <a href="#-project-structure">Structure</a> •
  <a href="#-contributing">Contributing</a>
</p>

---

<p align="center">
  <img src="https://github.com/kashsightplatform/kslearn/blob/main/screenshots/main_menu.png" alt="Main Menu" width="500" />
</p>

---

## ✨ What is kslearn?

> **kslearn** is an **offline-first educational learning system** that combines comprehensive study notes, interactive quizzes, flashcards, step-by-step tutorials, hierarchical courses with progression gating, AI chat with proactive suggestions, and **KSL-Verse** — a full RPG-style multiverse learning game — all in one terminal app.

| Attribute | Detail |
|:---|:---|
| 🎯 **Purpose** | Learn anything — study, don't memorize |
| 🌐 **Connectivity** | 100% offline-first (AI Chat optional) |
| 💻 **Platform** | Linux, macOS, Windows, Android (Termux) |
| 🐍 **Language** | Python 3.7+ |
| 📦 **Dependencies** | `rich`, `click` |

---

## 🚀 Features

### 📚 Core Learning Suite

| Feature | Icon | Description |
|:---|:---:|:---|
| **Course Catalog** | 📂 | 6-level hierarchical courses with progression gating & AI tutor |
| **Study Notes** | 📚 | 50+ topics across multiple subjects with reading time tracking |
| **Quizzes** | 📝 | Multiple-choice with explanations, timed mode, assessments |
| **AI Chat** | 🤖 | 11 AI providers (5 free) with proactive "What to Study Next" |
| **My Progress** | 📊 | Analytics dashboard, quiz scores, achievements, export report |
| **Study Tools** | 🔖 | Bookmarks, global search, spaced review system |
| **Knowledge Brain** | 🧠 | Offline Q&A database with auto-save from AI chat |
| **Data Store** | 🏪 | Download free & premium content packages |
| **Profiles** | 👤 | Multiple users, separate progress, profile-scoped data |
| **Settings** | ⚙️ | Theme, daily goal, API provider, spaced review limit |

---

### 🌌 KSL-Verse — Multiverse Learning Game

> **A full RPG-style game where learning is an adventure.**

#### 🎮 Game Modes

| Mode | XP Multiplier | Difficulty | Description |
|:---|:---:|:---:|:---|
| ⚔️ **Story Mode** | 1× | 🟢 Relaxed pace, hints available |
| ⚔️ **Normal** | 1× | 🟡 Standard experience |
| 🔥 **Hard Mode** | 1.5× | 🔴 No hints, no forgiveness |
| 💀 **Ironman** | 2× | ⚫ One wrong = run ends |
| 🏃 **Marathon** | 3× | ⚫ Full world back-to-back |
| ⚔️ **Boss Rush** | 2× | 🔴 Fight all bosses in sequence |
| ♾️ **Endless** | 1× | ⚫ Infinite scenarios, one wrong = game over |
| 💀 **Survival** | 1× | 🔴 3 lives — wrong answers cost lives |
| 🎲 **Randomizer** | 1× | 🟡 10 random shuffled scenarios |
| 🏃 **Practice** | 0× | 🟢 No penalties — just learning |

#### 🏆 Player Progression

| Level | Rank | XP Required | Badge |
|:---:|:---|:---:|:---:|
| 1 | Novice Walker | 0 | 🌱 |
| 2 | Apprentice Explorer | 200 | 🔍 |
| 3 | Seasoned Voyager | 500 | 🧭 |
| 5 | Realm Wanderer | 2,000 | 🗺️ |
| 7 | Cosmos Sage | 5,500 | 🌟 |
| 10 | Verse Transcendent | 20,000 | 👑 |

#### 🎯 Game Features

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
- **32 achievements** across 4 rarity tiers

---

### 🔥 AI-Powered Addictive Suggestions

> Every interaction proactively suggests what to learn next.

| Trigger | Suggestion Type | Example |
|:---|:---|:---|
| After AI Chat | 📚 Topic recommendations | *"Based on your question, try these next..."* |
| After Quiz | ⚠️ Weak area review | *"You scored 70% — focus on these areas..."* |
| After Course | 🔗 Related courses | *"Since you're exploring this topic, check these out..."* |
| After Sub-topic | 📅 Spaced review | *"1 topic due for review today"* |
| After Search | 🎯 Related content | *"Based on your search, here's what might interest you..."* |
| Streak ≥ 3 days | 🔥 Challenge | *"Try a timed quiz to push your limits!"* |

---

## 📋 Main Menu

| # | Option | Shortcut | Description |
|:---:|:---|:---:|:---|
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
# Install (30 seconds)
pip install -e .

# Launch
kslearn

# Launch KSL-Verse directly
kslearn verse
```

---

## 📥 Installation

### Prerequisites

| Requirement | Version | Notes |
|:---|:---:|:---|
| **Python** | 3.7+ | Required |
| **rich** | Latest | Terminal UI library |
| **click** | Latest | CLI framework |

### From Source

```bash
# Clone repository
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
# Install prerequisites
pkg install python

# Install dependencies
pip install rich click

# Clone and install
git clone https://github.com/kashsightplatform/kslearn.git
cd kslearn
pip install -e .

# Run
kslearn
```

> 📖 **Full installation guide:** See [docs/INSTALLATION.md](docs/INSTALLATION.md) for detailed instructions, troubleshooting, and all platforms.

---

## 🌌 KSL-Verse Deep Dive

### 🗺️ World Structure

Each world is a `*_verse.json` file in `data/ksl/`:

```
WebDev Cosmos 🌐
├── Level 1: The HTML Highlands 🏔️    (5 scenarios + mini-boss)
├── Level 2: The CSS Canyons 🎨        (5 scenarios + mini-boss)
├── Level 3: The JavaScript Junction ⚡ (5 scenarios + mini-boss)
├── Level 4: The DOM Delta 🌊          (5 scenarios + mini-boss)
├── Level 5: The Async Abyss 🔮        (5 scenarios + mini-boss)
└── Boss: The Chrono Phantom ⚔️        (5 questions, 150 XP)
```

### 🤖 AI World Generator

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  Course Catalog │ ──► │  AI Generation   │ ──► │  Playable World │
│  (data/ksl/)    │     │  (ThreadPool)    │     │  (*_verse.json) │
└─────────────────┘     └──────────────────┘     └─────────────────┘
```

**Process:**
1. **Browse Course Catalog** — Select any hierarchical course
2. **AI generates in parallel** — Uses `tgpt/sky` with `ThreadPoolExecutor`
3. **Each course category → a game level** — 5 scenarios per level + mini-boss
4. **Boss battle** — Covers all course concepts
5. **Lore entries + epilogue** — Inspired by course content

### 📄 Content Format

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

Build and manage encrypted `.ksl` packages:

| Command | Description |
|:---|:---|
| `python ksl_tool.py build data/my_subject.json -o data/my_subject.ksl` | Build encrypted package |
| `python ksl_tool.py verify data/my_subject.ksl` | Verify package integrity |
| `python ksl_tool.py info data/my_subject.ksl` | Display package information |
| `python ksl_tool.py pack my_course.json -t "Course Title"` | Pack course interactively |

---

## 🌐 Website

Visit **[kash-sight.web.app](https://kash-sight.web.app)** for:

| Page | Purpose |
|:---|:---|
| 🏠 **Home** | Project showcase and hero section |
| 📚 **KSL Store** | Free & premium content marketplace |
| 🏆 **LearnQuest** | Quiz-to-reward system |
| 📝 **Submit KSL** | Community content submissions |
| 💬 **Contact** | Suggestions, feedback, support |

---

## 🤝 Contributing

> ⚠️ **Note:** kslearn is **proprietary software** owned by KashSight Platform. We do not accept code contributions.

However, we **welcome feedback**:

| Type | How to Submit |
|:---|:---|
| 🐛 **Bug Report** | Use [Bug Report Template](.github/ISSUE_TEMPLATE/bug_report.md) |
| 💡 **Feature Request** | Use [Feature Request Template](.github/ISSUE_TEMPLATE/feature_request.md) |
| 📧 **Email** | kashsightplatform@gmail.com |
| 🌐 **Website** | https://kash-sight.web.app |

---

## 📄 License

**Proprietary** — KashSight Platform

All rights reserved. No modifications, redistributions, or derivative works permitted.

See [LICENSE](LICENSE) for full terms.

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/kashsightplatform">KashSight</a>
</p>

<p align="center">
  <sub>Learn anything. Study, don't memorize. 🚀</sub>
</p>
