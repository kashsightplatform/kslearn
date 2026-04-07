# kslearn User Guide

## Main Menu

Launch kslearn with:
```bash
kslearn
```

### Menu Structure

| # | Option | Shortcut | Description |
|---|--------|----------|-------------|
| 1 | 📂 Course Catalog | `1` / `CC` | 6-level hierarchical courses with progression gating, AI tutor, mark-as-complete |
| 2 | 📚 Study Notes | `2` / `N` | Browse comprehensive learning materials with reading time tracking |
| 3 | 📝 Take Quiz | `3` / `Q` | Test your knowledge with interactive quizzes |
| 4 | 🤖 AI Chat | `4` | Chat with AI tutor — 11 providers, offline & online modes |
| 5 | 📊 My Progress | `5` / `P` | **Merged:** Analytics dashboard, quiz scores, achievements, export report |
| 6 | 🔖 Study Tools | `6` / `T` | **Merged:** Bookmarks, global search, spaced review |
| 7 | 🧠 Knowledge Brain | `7` / `B` | Offline AI Q&A database with auto-save |
| 8 | 🏪 Data Store | `8` | Download free & premium courses |
| S | ❤️ Support | `S` | Credits, email, website & GitHub |
| F | 🎮 Study Modes | `F` / `M` | **Merged:** Flashcards, timed quiz, tutorials |
| D | 👤 Profiles | `D` | Switch or manage user profiles |
| C | ⚙️ Settings | `C` | Configure theme, daily goal, API provider, spaced review limit |
| H | ❓ Help | `H` | Show commands and usage info |
| 0 | ❌ Exit | `0` | Leave kslearn (with confirmation) |

### Sub-menus

#### 📊 My Progress (Option 5 / P)
| # | Option | Description |
|---|--------|-------------|
| 1 | 📈 Analytics Dashboard | Visual charts, heatmaps, weak areas, insights |
| 2 | 📋 Quiz Scores | Detailed quiz history & accuracy |
| 3 | 🏆 Achievements | Badges, milestones, rarity breakdown |
| 4 | 📄 Export Report | Generate Markdown progress summary |
| 0 | Back | Return to main menu |

#### 🔖 Study Tools (Option 6 / T)
| # | Option | Description |
|---|--------|-------------|
| 1 | 🔖 Bookmarks | Saved topics for quick review |
| 2 | 🔍 Global Search | Search all notes at once |
| 3 | 📅 Spaced Review | Revisit topics you struggled with |
| 0 | Back | Return to main menu |

#### 🎮 Study Modes (Option F / M)
| # | Option | Description |
|---|--------|-------------|
| 1 | 🃏 Flashcards | Card-based review with flip reveal |
| 2 | ⚡ Timed Quiz | 60-second speed challenge |
| 3 | 🎓 Tutorials | Interactive step-by-step lessons |
| 0 | Back | Return to main menu |

## Course Catalog Features

When viewing a course, you have additional options:

| Key | Action |
|-----|--------|
| `1-9` | Select a category |
| `G` | 📖 View Glossary |
| `C` | 📋 View Case Studies |
| `M` | 🎬 View Media |
| `R` | 📎 View Resources |
| `D` | 💬 View Discussion Prompts |
| `A` | 🤖 Ask AI about this course (offline/online) |
| `S` | 📊 Course Stats |
| `0` | Back to Course Catalog |

### Course Catalog Main Menu
| Key | Action |
|-----|--------|
| `S` | Search courses by keyword |
| `F` | Filter by difficulty (beginner/intermediate/advanced/expert) |
| `L` | Continue where you left off (last visited course) |
| `R` | Reset filters |

### Sub-topic Actions
| Key | Action |
|-----|--------|
| `X` | ✅ Mark as Complete (hidden if already completed) |
| `B` | Back to Sub-topics |
| `0` | Back to Main Menu |

## AI-Powered Suggestions

After every interaction, kslearn shows personalized "What to Study Next" suggestions:

- **After AI Chat** → "Based on your question, try these next..."
- **After Quiz** → "You scored X% — here's what to focus on"
- **After Course View** → "Since you're exploring this topic, check these out..."
- **After Sub-topic Complete** → "You're making progress! Keep going with..."
- **After Search** → "Based on your search, here's what might interest you..."
- **Streak ≥ 3 days** → "🔥 Streak Challenge — try a timed quiz!"
- **Spaced Review Due** → "📅 X topics are due for review today"

See [AI_SUGGESTIONS.md](AI_SUGGESTIONS.md) for full details.

## Themes

kslearn supports 3 UI themes. Change in Settings (C) → edit `theme`:

| Theme | Description |
|-------|-------------|
| `sky_blue` | Clean, bright blue tones (default) |
| `green` | Forest green, nature-inspired |
| `grey` | Minimalist monochrome |

> **Note:** Theme changes apply immediately when you save settings.

## Shortcut Key Reference

All shortcut keys are unique — no collisions:

| Key | Routes To |
|-----|-----------|
| `1` / `CC` | Course Catalog |
| `2` / `N` | Study Notes |
| `3` / `Q` | Take Quiz |
| `4` | AI Chat |
| `5` / `P` | My Progress (merged) |
| `6` / `T` | Study Tools (merged) |
| `7` / `B` | Knowledge Brain |
| `8` | Data Store |
| `S` | Support |
| `F` / `M` | Study Modes (merged) |
| `D` | Profiles |
| `C` | Settings |
| `H` / `?` | Help |
| `0` | Exit |

## Data Store

Download new courses from: `https://kashsight-4cbb8.web.app/kslearn.html`

## Progress Tracking Keys

| Key Pattern | Type | Stored When |
|-------------|------|-------------|
| `hier_{subtopic_id}` | Sub-topic completion | User presses `[X]` Mark as Complete |
| `hier_outcome_{outcome_id}` | Outcome quiz result | Assessment quiz completed |
| `reading_{category}_{topic}` | Reading time | User leaves a notes topic (5s+ spend) |
| `notes_quiz_{category}_{timestamp}` | Notes quiz result | Notes quiz completed |
| `profile_{name}_{key}` | Profile-scoped data | When using user profiles |
