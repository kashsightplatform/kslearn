# AI-Powered "What to Study Next" — kslearn

## Overview

kslearn features an **AI-powered suggestion engine** that proactively recommends what to learn next after every interaction. The goal is to make learning **addictive** — always showing you the logical next step so you never run out of momentum.

## How It Works

The suggestion engine analyzes your current context and generates personalized recommendations based on:

1. **Topic Detection** — Keywords in your question/quiz/search
2. **Quiz Performance** — Weak areas scored below 80%
3. **Study Streak** — Momentum-based challenges
4. **Spaced Review Timing** — Topics due for review (1-3 days since completion)
5. **Course Relationships** — Shared tags and categories
6. **Beginner Defaults** — If no data, suggest popular starter courses

## Where Suggestions Appear

### 1. After AI Chat 💬
**Trigger:** You ask the AI tutor a question  
**Detection:** Keyword matching across 10 topic areas  
**Suggestions:** 3-4 cards with specific next steps

**Example:**
```
You: "What are Python variables?"
AI: [Explains variables with examples]

✨ Keep Learning
─────────────────────────────────────
🎓 AI Tutor Suggests:

Based on your question, here's a great next step:

📚 Learn about Functions & Scope
   Master reusable code blocks

📝 Try a Python Quiz
   Test your knowledge with 5 questions

🔧 Build a Mini Project
   Apply what you've learned in practice
```

### 2. After Quiz Completion 📝
**Trigger:** You finish any quiz  
**Detection:** Score analysis — identifies weak areas (<80%)  
**Suggestions:** Review recommendations + related topics

**Example:**
```
📊 Quiz Results
Score: 7/10 (70%)

✨ What to Study Next
─────────────────────────────────────
🤖 AI Tutor Says:

Great effort! Here's what to focus on next:

⚠️ Review: Variables and Data Types
   You scored 65% — try again to reach 80%+
   💡 Weak area — practice makes perfect!

📚 Introduction to JavaScript
   Shares 2 topic(s): programming, beginner
   🔓 New • 180 min

🔥 Streak Challenge
   You're on a 3-day streak! Try a timed quiz
   ⚡ You're on fire — push your limits!

Quick actions:
[R] Start spaced review
[T] Take timed quiz challenge
[0] Continue
```

### 3. After Course Viewing 📂
**Trigger:** You browse a hierarchical course  
**Detection:** Course tags and category matching  
**Suggestions:** Related courses with shared topics

**Example:**
```
📂 Introduction to Python Programming

✨ What to Study Next
─────────────────────────────────────
🤖 AI Tutor Says:

Since you're exploring this topic, check these out:

🐍 Advanced Python Programming
   Shares 2 topic(s): python, programming
   🔓 New • 240 min

🌐 Web Development Fundamentals
   Shares 1 topic(s): programming, beginner
   ✅ In Progress • 180 min
```

### 4. After Sub-topic Complete ✅
**Trigger:** You press "Mark as Complete" `[X]`  
**Detection:** Course tags + progress momentum  
**Suggestions:** Next logical step in learning path

**Example:**
```
✅ Marked as complete!

✨ What to Study Next
─────────────────────────────────────
🤖 AI Tutor Says:

You're making progress! Keep the momentum going:

📝 Quick Quiz: Variables
   Test your understanding before moving on
   🔓 New • 5 min

📅 Spaced Review
   1 topic(s) are due for review today
   🧠 Perfect timing — review now to lock it in memory
```

### 5. After Global Search 🔍
**Trigger:** You search all notes  
**Detection:** Search term + result categories  
**Suggestions:** Related content based on search results

**Example:**
```
🔍 Global Search
Search term: python

Found 5 result(s):

  1. Programming > Variables
     ...Python has several built-in data types...

  2. Programming > Functions
     ...A function is a reusable block of code...

✨ What to Study Next
─────────────────────────────────────
🤖 AI Tutor Says:

Based on your search, here's what might interest you:

📚 Web Development Fundamentals
   Shares 1 topic(s): programming
   🔓 New • 180 min

📝 Take a Programming Quiz
   Test your knowledge
```

### 6. Streak Challenge 🔥
**Trigger:** Study streak ≥ 3 days  
**Detection:** `study_streak.current` in config  
**Suggestions:** Timed quiz challenge

### 7. Spaced Review Reminder 📅
**Trigger:** 1-3 days since last completion of a sub-topic  
**Detection:** `completed_at` timestamps in `learning_progress`  
**Suggestions:** Review specific topics to lock in memory

## Topic Detection Matrix

| Topic | Keywords Detected |
|-------|------------------|
| Python | `python`, `variable`, `function`, `loop`, `class`, `object`, `list`, `dict`, `code` |
| Math | `math`, `algebra`, `calculus`, `equation`, `derivative`, `integral`, `geometry` |
| Science | `physics`, `chemistry`, `biology`, `atom`, `molecule`, `cell`, `energy` |
| Web Dev | `html`, `css`, `javascript`, `react`, `node`, `web`, `browser`, `frontend` |
| Data Science | `data`, `analysis`, `statistics`, `probability`, `pandas`, `numpy`, `ml` |
| History | `history`, `war`, `empire`, `civilization`, `ancient`, `medieval`, `revolution` |
| Psychology | `psychology`, `mind`, `behavior`, `cognitive`, `therapy`, `mental`, `emotion` |
| Music | `music`, `chord`, `scale`, `rhythm`, `melody`, `harmony`, `instrument` |
| Business | `business`, `marketing`, `sales`, `revenue`, `profit`, `startup`, `strategy` |
| Language | `grammar`, `vocabulary`, `language`, `learn english`, `speak`, `pronounce` |

## Suggestion Types

| Type | Icon | When Shown |
|------|------|------------|
| Related Course | 📚 | Tag/category overlap detected |
| Weak Area Review | 📝 | Quiz score < 80% |
| Practice/Project | 🔧 | After learning new concept |
| Explore Next | 📖 | Natural progression path |
| Style/Best Practice | 💡 | Code or writing topics |
| Streak Challenge | 🔥 | Streak ≥ 3 days |
| Spaced Review | 📅 | 1-3 days since completion |
| Beginner Default | 🌟 | No data available |

## Quick Actions

After suggestions are displayed, you can:

| Key | Action |
|-----|--------|
| `C` | Browse suggested courses |
| `R` | Start spaced review immediately |
| `T` | Take timed quiz challenge |
| `S` | Show suggestions again |
| `0` | Continue to main menu |

## Files Involved

| File | Purpose |
|------|---------|
| `kslearn/engines/notes_viewer.py` | `show_ai_suggestions()` — main suggestion engine for courses |
| `kslearn/engines/notes_viewer.py` | `search_all_notes()` — global search across all content |
| `kslearn/main/ai_chat.py` | `_generate_learning_suggestions()` — AI chat suggestions |
| `kslearn/cli.py` | `_run_global_search()` — search with AI suggestions |
| `kslearn/cli.py` | `_run_quiz_interactive()` — quiz with post-quiz suggestions |
| `kslearn/cli.py` | `_run_my_progress()` — merged progress menu |
| `kslearn/cli.py` | `_run_study_tools()` — merged study tools menu |
| `kslearn/cli.py` | `_run_study_modes()` — merged study modes menu |

## Customization

Suggestions are driven by:
- **Course tags** — Add more tags to your `.ksl` courses for better matching
- **Quiz performance** — The more you quiz, the better the weak-area detection
- **Study patterns** — Streaks and spaced review timing are personalized

To extend topic detection, add new entries to the `topic_keywords` dict in:
- `kslearn/engines/notes_viewer.py` (`show_ai_suggestions`)
- `kslearn/main/ai_chat.py` (`_generate_learning_suggestions`)
