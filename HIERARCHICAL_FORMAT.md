# Hierarchical Course Structure — kslearn

## Overview

kslearn supports **6-level hierarchical navigation** for course content with **progression gating** — you can't advance to the next level until you meet requirements (min_score, prerequisites, sequential completion).

## The Hierarchy

```
Level 1: Course
  └── Level 2: Category (Unit Category)
       └── Level 3: Unit
            └── Level 4: Learning Outcome
                 └── Level 5: Sub-topic (Performance Standard)
                      └── Level 6: Content (actual text, examples, code)
```

## Progression Gating (Locking System)

| Gate | Level | Rule |
|------|-------|------|
| **Prerequisites** | Course | Must complete prerequisite courses first |
| **Prerequisites** | Unit | Must complete prerequisite units (with optional min_score) |
| **Sequential** | Learning Outcome | Must pass previous outcome with `min_score`% before unlocking next |
| **Must Complete All** | Learning Outcome | If set, ALL previous outcomes must pass `min_score` |

Lock indicators: 🔒 = Locked, 🔓 = Available

## Complete JSON Structure

See `data/ksl/hierarchical_sample.json` for a working example with all fields.

### Key Fields at Each Level

| Level | Key Fields |
|-------|-----------|
| **Course** | `id`, `code`, `title`, `description`, `icon`, `prerequisites[]`, `difficulty`, `estimated_minutes`, `credits`, `tags[]`, `learning_styles[]`, `glossary[]`, `media[]`, `resources[]`, `instructor_notes`, `completion_requirements{min_score, must_complete_all}`, `version`, `changelog` |
| **Category** | `id`, `title`, `description`, `difficulty`, `estimated_minutes`, `glossary[]`, `case_studies[]`, `discussion_prompts[]` |
| **Unit** | `id`, `code`, `title`, `description`, `prerequisites[]`, `difficulty`, `estimated_minutes`, `tools[]`, `equipment[]`, `supplies[]`, `performance_standards[]`, `glossary[]`, `case_studies[]`, `media[]`, `resources[]`, `discussion_prompts[]`, `completion_requirements`, `instructor_notes` |
| **Learning Outcome** | `id`, `title`, `description`, `min_score`, `must_complete_all`, `estimated_minutes`, `difficulty`, `discussion_prompts[]`, `case_studies[]`, `media[]` |
| **Sub-topic** | `id`, `title`, `type`, `content`, `key_points[]`, `examples[]`, `quiz[]`, `difficulty`, `estimated_minutes`, `learning_styles[]`, `media[]`, `resources[]`, `discussion_prompts[]` |

## Sub-topic Types

| Type | Icon | Purpose | Runnable |
|------|------|---------|----------|
| `content` | 📄 | Main learning content | No |
| `example` | 💡 | Illustrative examples | No |
| `activity` | 🔧 | Hands-on exercises | No |
| `assessment` | 📝 | Quizzes and tests | ✅ Yes — runs quiz inline |
| `reference` | 📎 | Additional resources | No |

## Assessment Quizzes in Sub-topics

Sub-topics of type `"assessment"` can include embedded `quiz[]` arrays. When the user opens the sub-topic, the quiz runs automatically with:
- Question-by-question display with streak tracking
- Score, accuracy, and best streak results
- Automatic save to `learning_progress` (key: `hier_outcome_{outcome_id}`)
- Achievement checks triggered on completion

## Mark as Complete

Every sub-topic content view includes an **✅ Mark as Complete** `[X]` option. When pressed:
- Saves to `learning_progress` with key `hier_{subtopic_id}`
- Records completion timestamp and full breadcrumb path

## Difficulty Levels

| Level | Icon |
|-------|------|
| `beginner` | 🟢 |
| `intermediate` | 🟡 |
| `advanced` | 🔴 |
| `expert` | ⚫ |

## Course Catalog Features

| Feature | Key | Description |
|---------|-----|-------------|
| **Search** | `[S]` | Text search across course titles, descriptions, and tags |
| **Filter** | `[F]` | Filter by difficulty (beginner/intermediate/advanced/expert) |
| **Continue** | `[L]` | Jump back to your last-visited course |
| **Reset** | `[R]` | Clear all active filters |

## How to Package

```bash
# Interactive
python ksl_tool.py

# CLI
python ksl_tool.py pack my_course.json -t "Course Title"
```

## How to Access

1. Launch: `kslearn` or `python -m kslearn`
2. Select **Option 1: Course Catalog**
3. Browse: **Course → Category → Unit → Outcome → Sub-topic → Content**
4. Extra actions: `[G]` Glossary, `[C]` Case Studies, `[M]` Media, `[R]` Resources, `[D]` Discussions, `[S]` Stats
5. Use `[S]` to search, `[F]` to filter by difficulty, `[L]` to continue last course

## Backward Compatibility

Existing flat-format `.ksl` files continue to work. Hierarchical is an additional content type.

## Progress Tracking Keys

| Key Pattern | Type | Stored When |
|-------------|------|-------------|
| `hier_{subtopic_id}` | Sub-topic completion | User presses `[X]` Mark as Complete |
| `hier_outcome_{outcome_id}` | Outcome quiz result | Assessment quiz completed |
| `reading_{category}_{topic}` | Reading time | User leaves a notes topic (5s+ spend) |
