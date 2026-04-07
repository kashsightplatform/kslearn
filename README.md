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
  <a href="https://github.com/kashsightplatform/kslearn"><img src="https://img.shields.io/badge/version-1.0.0-cyan.svg" alt="Version 1.0.0" /></a>
</p>

---

## ✨ What is kslearn?

kslearn is an **offline-first educational learning system** that combines comprehensive study notes, interactive quizzes, flashcards, step-by-step tutorials, hierarchical courses with progression gating, and AI chat with proactive suggestions — all in one terminal app.

**No internet required.** Everything works locally. Only the AI Chat feature may need a connection (or use the built-in offline mode).

<p align="center">
  <img src="https://github.com/kashsightplatform/kslearn/blob/main/screenshots/main_menu.png" alt="Main Menu" width="500" />
  <br /><em>kslearn main menu — streamlined, merged, AI-powered</em>
</p>

---

## 🚀 Features

| Feature | Description |
|---------|-------------|
| 📂 **Course Catalog** | 6-level hierarchical courses with progression gating, AI tutor, mark-as-complete |
| 📚 **Study Notes** | 50+ topics across multiple subjects with reading time tracking |
| 📝 **Quizzes** | Multiple-choice with explanations, timed mode, assessment quizzes in courses |
| 🤖 **AI Chat** | 11 AI providers (5 free) with **proactive "What to Study Next" suggestions** |
| 📊 **My Progress** | **Merged:** Analytics dashboard, quiz scores, achievements, export report |
| 🔖 **Study Tools** | **Merged:** Bookmarks, global search, spaced review |
| 🧠 **Knowledge Brain** | Offline Q&A database with auto-save from AI chat |
| 🏪 **Data Store** | Download free & premium courses |
| ❤️ **Support** | Credits, email, website, GitHub |
| 🎮 **Study Modes** | **Merged:** Flashcards, timed quiz, tutorials |
| 👤 **Profiles** | Multiple users, separate progress, profile-scoped keys |
| ⚙️ **Settings** | Theme, daily goal, API provider, spaced review limit |

### 🔥 New: AI-Powered Addictive Suggestions

Every interaction with kslearn now proactively suggests what to learn next:

- **After AI Chat** → "Based on your question, try these next: Learn about X, Take a quiz on Y, Build a project with Z"
- **After Quiz** → "You scored 75% — here's what to focus on next"
- **After Course View** → "Since you're exploring Python, check out these related courses"
- **After Sub-topic Complete** → "You're making progress! Keep the momentum going with these"
- **After Search** → "Based on your search for 'variables', here's what might interest you"
- **Streak Challenge** → "You're on a 3-day streak! Try a timed quiz to keep it going"
- **Spaced Review** → "2 topics are due for review today — perfect timing to lock it in memory"

---

## 📋 Main Menu

| # | Option | Shortcut | Description |
|---|--------|----------|-------------|
| 1 | 📂 Course Catalog | `1` / `CC` | Hierarchical courses with AI tutor, progression gating |
| 2 | 📚 Study Notes | `2` / `N` | Browse comprehensive learning materials |
| 3 | 📝 Take Quiz | `3` / `Q` | Test your knowledge |
| 4 | 🤖 AI Chat | `4` | Chat with AI tutor (online & offline) |
| 5 | 📊 My Progress | `5` / `P` | **Merged:** Analytics, quiz scores, achievements, export |
| 6 | 🔖 Study Tools | `6` / `T` | **Merged:** Bookmarks, global search, spaced review |
| 7 | 🧠 Knowledge Brain | `7` / `B` | Offline AI Q&A database |
| 8 | 🏪 Data Store | `8` | Download new content (Free & Premium) |
| S | ❤️ Support | `S` | Credits, email, website & GitHub |
| F | 🎮 Study Modes | `F` / `M` | **Merged:** Flashcards, timed quiz, tutorials |
| D | 👤 Profiles | `D` | Switch or manage user profiles |
| C | ⚙️ Settings | `C` | Configure your experience |
| H | ❓ Help | `H` | Show commands and usage info |
| 0 | ❌ Exit | `0` | Leave kslearn |

---

## 📦 Quick Start

```bash
# Install
pip install -e .

# Launch
kslearn
```

That's it. Start learning.

---

## 📥 Installation

### Termux (Android)
```bash
pkg install python
git clone https://github.com/kashsightplatform/kslearn
cd kslearn
pip install -e .
kslearn
```

### Linux / macOS
```bash
git clone https://github.com/kashsightplatform/kslearn
cd kslearn
pip install -e .
kslearn
```

### Windows
```cmd
git clone https://github.com/kashsightplatform/kslearn
cd kslearn
pip install -e .
kslearn
```

### Verify
```bash
kslearn --version
```

---

## 🎮 Usage

| Command | Action |
|---------|--------|
| `kslearn` | Launch interactive menu |
| `kslearn play` | Start learning |
| `kslearn quiz <topic>` | Start specific quiz |
| `kslearn study` | Browse notes |
| `kslearn brain` | View knowledge brain |
| `kslearn track` | View learning tracks |
| `kslearn config` | View/edit settings |
| `kslearn --version` | Show version |
| `kslearn --help` | Show help |

### ⌨️ Keyboard Shortcuts

| Key | Feature |
|-----|---------|
| `1-8` | Main menu options |
| `F` | Flashcards |
| `T` | Timed Quiz |
| `G` | Global Search |
| `R` | Spaced Review |
| `U` | Tutorials |
| `V` | Achievements |
| `E` | Export Report |
| `D` | Profiles |
| `C` | Settings |
| `H` | Help |
| `0` | Exit |

---

## 🛠️ Content Creation with `ksl_tool.py`

kslearn uses **`.ksl` files** — encrypted, signed content packages that users cannot modify. As a content creator, you build `.ksl` files from JSON source files.

### Prerequisites

```bash
pip install rich
```

### Step 1: Create Your JSON Content

Create a JSON file with your content. Structure:

```json
{
  "metadata": {
    "category": "my_subject",
    "title": "📖 My Subject",
    "description": "Description of this subject",
    "icon": "📖",
    "difficulty": "beginner",
    "version": "1.0",
    "author": "Your Name"
  },
  "notes": [
    {
      "id": 1,
      "title": "Introduction",
      "icon": "📌",
      "content": "Full content with\nnewlines and formatting.",
      "key_points": ["Point 1", "Point 2"],
      "examples": [
        {
          "title": "Example Title",
          "explanation": "How this works.",
          "code": "example code or text"
        }
      ]
    }
  ],
  "quizzes": [
    {
      "title": "Introduction Quiz",
      "questions": [
        {
          "question": "What is this?",
          "options": ["A", "B", "C", "D"],
          "correct": 0,
          "explanation": "Here's why A is correct."
        }
      ]
    }
  ],
  "flashcards": [
    {
      "topic": "Introduction",
      "cards": [
        {"front": "What is X?", "back": "X is...", "difficulty": "easy"}
      ]
    }
  ],
  "tutorials": [
    {
      "title": "Getting Started",
      "steps": [
        {"title": "Step 1", "content": "First step details."}
      ]
    }
  ]
}
```

### Step 2: Build the `.ksl` File

```bash
python ksl_tool.py build data/my_subject.json -o data/my_subject.ksl
```

### Step 3: Verify

```bash
python ksl_tool.py verify data/my_subject.ksl
```

### Encrypting Content (Optional — for premium/protected content)

```bash
python encrypt_content.py data/my_subject.json
```

### Commands Reference

| Command | Description |
|---------|-------------|
| `python ksl_tool.py build <json> -o <output.ksl>` | Build a .ksl package |
| `python ksl_tool.py verify <file.ksl>` | Verify signature & integrity |
| `python ksl_tool.py info <file.ksl>` | Show package metadata |
| `python encrypt_content.py <json>` | Encrypt content for protection |
| `python pdf_to_ksl.py <pdf>` | Convert PDF to .ksl format |

---

## 📂 Project Structure

```
kslearn/
├── kslearn/                # Python application
│   ├── cli.py              # Main CLI entry point
│   ├── config.py           # Configuration management
│   ├── loader.py           # Content loader (.ksl + JSON)
│   ├── ui.py               # Rich UI components with theming
│   ├── main.py             # Application bootstrap
│   ├── engines/            # Learning engines
│   │   ├── quiz_engine.py      # Quiz processing
│   │   ├── notes_viewer.py     # Note rendering
│   │   ├── tutorials.py        # Tutorial engine
│   │   └── achievements.py     # Badge system
│   └── main/               # Feature modules
│       ├── ai_chat.py          # AI tutor (online/offline)
│       ├── datastore.py        # Content store
│       ├── support.py          # Social links
│       └── learning_notes.py   # Notes redirect
├── data/                   # Content & config
│   ├── *.json              # Content packages (source)
│   ├── *.ksl               # Encrypted content packages
│   ├── brain/              # Offline knowledge base
│   └── config/             # User settings, themes, AI providers
├── docs/                   # Documentation
├── public/                 # Website (Firebase hosting)
├── ksl_tool.py             # Content builder tool
├── encrypt_content.py      # Content encryption tool
├── pdf_to_ksl.py           # PDF to .ksl converter
└── setup.py                # Package installation
```

---

## 📚 Documentation

| Document | Description |
|----------|-------------|
| [📖 User Guide](docs/USER_GUIDE.md) | Complete feature walkthrough |
| [🎨 Design](docs/DESIGN.md) | Architecture and design decisions |
| [📦 Installation](docs/INSTALLATION.md) | Detailed setup instructions |
| [➕ Adding Content](docs/ADDING_CONTENT.md) | How to create your own content |
| [🔒 Protection](docs/PROTECTION.md) | Content encryption and security |

---

## 🗺️ Roadmap — Upcoming Updates

### ✅ Recently Completed

| Update | Status |
|--------|--------|
| **✅ 📂 Hierarchical Course Navigation** | 6-level drill-down: Course → Category → Unit → Learning Outcome → Sub-topic → Content with progression gating (lock/unlock), glossary, case studies, media, resources, discussions, and stats |

### 🔥 Coming Soon

| Update | Details |
|--------|---------|
| **🧑‍🏫 Multiplayer Leaderboards** | Compete with friends, global & local rankings, weekly challenges |
| **📊 Analytics Dashboard** | Visual charts for learning habits, weak areas, time-per-topic |

### 🚀 On the Horizon

| Update | Details |
|--------|---------|
| **🎙️ Voice Mode** | Listen to notes aloud, voice-activated quizzes, hands-free learning |
| **🌐 Multi-language Support** | Translations for Swahili, French, Spanish, Arabic — study in your language |
| **📱 Mobile App (GUI)** | Native Android/iOS app with the same content — no terminal required |

### 💡 Planned

| Update | Details |
|--------|---------|
| **🎮 Gamified Learning Paths** | Unlock worlds, earn XP, level up your knowledge tree |
| **📥 Import/Export Content** | Share custom `.ksl` packs with friends or community |
| **🔌 Plugin System** | Extend kslearn with custom learning engines & themes |

---

## 🤝 Feedback & Suggestions

kslearn is proprietary software — we don't accept code contributions or pull requests. But we **love feedback**!

- 🐛 [Report a bug](.github/ISSUE_TEMPLATE/bug_report.md)
- 💡 [Suggest a feature](.github/ISSUE_TEMPLATE/feature_request.md)
- 📧 Email us: kashsightplatform@gmail.com

---

## 📜 License

**Proprietary — KashSight Platform.** This software is provided for **personal learning use only**. No modifying, redistributing, or creating derivative works. See [LICENSE](LICENSE) for full terms.

Found a bug or have a feature request? [Report it here](https://github.com/kashsightplatform/kslearn/issues) or email us at kashsightplatform@gmail.com.

---

## 📬 Contact

- **Email:** kashsightplatform@gmail.com
- **Socials:** [@kash.sight](https://instagram.com/kash.sight)
- **Website:** https://kash-sight.web.app
- **Company:** KashSight Platform

---

## 💝 Support This Project

If kslearn has helped you learn, consider supporting its development. Every contribution keeps this project free and updated:

<p align="center">
  <a href="https://github.com/sponsors/kashsightplatform" title="GitHub Sponsors">
    <img src="https://img.shields.io/badge/GitHub%20Sponsors-Support%20Us-1000?style=for-the-badge&logo=githubsponsors&logoColor=EA4AAA" height="45" />
  </a>
  &nbsp;&nbsp;
  <a href="https://ko-fi.com/kashsightplatform" title="Ko-fi">
    <img src="https://img.shields.io/badge/Ko--fi-Buy%20Me%20a%20Coffee-FF5E5B?style=for-the-badge&logo=ko-fi&logoColor=white" height="45" />
  </a>
  &nbsp;&nbsp;
  <a href="https://paypal.me/kashsightplatform" title="PayPal">
    <img src="https://img.shields.io/badge/PayPal-Donate%20Now-00457C?style=for-the-badge&logo=paypal&logoColor=white" height="45" />
  </a>
  &nbsp;&nbsp;
  <a href="https://selar.co/kashsightplatform" title="Selar">
    <img src="https://img.shields.io/badge/Selar-Support%20Us-FF6F00?style=for-the-badge&logo=shopify&logoColor=white" height="45" />
  </a>
  &nbsp;&nbsp;
  <a href="mailto:kashsightplatform@gmail.com?subject=kslearn%20Donation" title="Email">
    <img src="https://img.shields.io/badge/Email-Us%20Directly-EA4335?style=for-the-badge&logo=gmail&logoColor=white" height="45" />
  </a>
</p>

---

<p align="center">Built with ❤️ by KashSight</p>
