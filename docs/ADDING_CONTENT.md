# 📝 Adding New Topics & Quizzes to kslearn

A complete guide to extending kslearn with new learning content.

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [File Structure](#file-structure)
3. [Adding Learning Notes](#adding-learning-notes)
4. [Adding Quizzes](#adding-quizzes)
5. [Adding Code Snippets](#adding-code-snippets)
6. [📚 Adding Hierarchical Courses](#adding-hierarchical-courses)
7. [Complete Example](#complete-example)
8. [Testing Your Content](#testing-your-content)
9. [Tips & Best Practices](#tips--best-practices)

---

## 🎯 Overview

kslearn uses **JSON files** to store all learning content, making it easy to add new topics without coding. You can add:

- **📚 Learning Notes** - Study materials with explanations
- **📝 Quizzes** - Multiple-choice questions with answers
- **💻 Code Snippets** - Reusable code examples
- **🏫 Hierarchical Courses** - 6-level course structures with progression gating

All files are stored in the `data/` directory.

---

## 📁 File Structure

```
kslearn/
├── data/
│   ├── notes/          # Learning notes (JSON)
│   │   ├── python.json
│   │   ├── ai_ml.json
│   │   └── your_topic.json    ← Add new here
│   │
│   ├── quizzes/        # Quiz questions (JSON)
│   │   ├── python.json
│   │   ├── ai_ml.json
│   │   └── your_topic.json    ← Add new here
│   │
│   └── snippets/       # Code examples (JSON)
│       ├── python.json
│       ├── ai_ml.json
│       └── your_topic.json    ← Add new here
│
└── kslearn/
    └── engines/
        ├── notes_viewer.py   # Notes display logic
        └── quiz_engine.py    # Quiz logic
```

---

## 📚 Adding Learning Notes

### Step 1: Create JSON File

Create a new file in `data/notes/your_topic.json`:

```json
{
  "metadata": {
    "category": "your_topic",
    "title": "📖 Your Topic Name",
    "description": "Brief description of what this topic covers",
    "icon": "📚",
    "difficulty": "beginner",
    "version": "1.0.0"
  },
  "topics": [
    {
      "id": 1,
      "title": "First Topic Title",
      "icon": "📄",
      "content": "Your learning content here. Explain concepts clearly with examples.\n\nYou can use multiple paragraphs.\n\n• Bullet points work too\n• Like this\n• Very flexible",
      "key_points": [
        "Important point 1",
        "Important point 2",
        "Important point 3"
      ],
      "examples": [
        {
          "title": "Example Title",
          "explanation": "What this example demonstrates",
          "code": "print('Hello, World!')",
          "output": "Hello, World!"
        }
      ]
    }
  ],
  "quizzes": [
    {
      "question": "What is the output of print('Hello')?",
      "options": ["Hello", "World", "Error", "None"],
      "answer": 0,
      "explanation": "print('Hello') outputs the string 'Hello' to the console."
    }
  ],
  "code_snippets": [
    {
      "title": "Snippet Title",
      "description": "What this snippet does",
      "code": "def hello():\n    return 'Hello'",
      "tags": ["functions", "basics"]
    }
  ]
}
```

### Step 2: Add Topics

Each topic in the `topics` array should have:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | number | ✅ | Unique identifier |
| `title` | string | ✅ | Topic title |
| `icon` | string | ❌ | Emoji icon (default: 📄) |
| `content` | string | ✅ | Learning material (use `\n` for line breaks) |
| `key_points` | array | ❌ | Important takeaways |
| `examples` | array | ❌ | Code examples with explanations |

### Step 3: Format Content

**Content Formatting Tips:**
- Use `\n\n` for paragraph breaks
- Use `•` for bullet points
- Use `\n` for line breaks within bullets
- Keep paragraphs short (3-5 lines)

**Example Content:**
```json
"content": "Variables store data values.\n\nBasic types:\n• str - Text strings\n• int - Whole numbers\n• float - Decimal numbers\n• bool - True or False"
```

---

## 📝 Adding Quizzes

### Step 1: Create Quiz JSON

Create a new file in `data/quizzes/your_topic.json`:

```json
{
  "metadata": {
    "category": "your_topic",
    "title": "📝 Your Topic Quiz",
    "description": "Test your knowledge",
    "version": "1.0.0",
    "passing_score": 70
  },
  "questions": {
    "Topic Name 1": [
      {
        "q": "Question text here?",
        "options": [
          "Option A",
          "Option B",
          "Option C",
          "Option D"
        ],
        "answer": 0,
        "exp": "Explanation of why this is correct"
      }
    ],
    "Topic Name 2": [
      {
        "q": "Another question?",
        "options": ["A", "B", "C", "D"],
        "answer": 2,
        "exp": "Explanation"
      }
    ]
  }
}
```

### Step 2: Add Questions

Each question should have:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `q` | string | ✅ | Question text |
| `options` | array | ✅ | 4 answer choices (index 0-3) |
| `answer` | number | ✅ | Correct option index (0-3) |
| `exp` | string | ✅ | Explanation of the answer |

### Question Format Examples

**Basic Question:**
```json
{
  "q": "What is Python?",
  "options": [
    "A programming language",
    "A snake",
    "A database",
    "A web framework"
  ],
  "answer": 0,
  "exp": "Python is a high-level programming language known for its simplicity."
}
```

**Code-Based Question:**
```json
{
  "q": "What is the output?\n\nx = 5\ny = 10\nprint(x + y)",
  "options": ["5", "10", "15", "50"],
  "answer": 2,
  "exp": "5 + 10 equals 15."
}
```

---

## 💻 Adding Code Snippets

### Step 1: Create Snippets JSON

Create a new file in `data/snippets/your_topic.json`:

```json
{
  "metadata": {
    "category": "your_topic",
    "title": "💻 Code Snippets",
    "version": "1.0.0"
  },
  "snippets": [
    {
      "title": "Function Example",
      "description": "How to define a function",
      "code": "def greet(name):\n    return f'Hello, {name}!'",
      "tags": ["functions", "basics", "strings"],
      "language": "python"
    }
  ]
}
```

### Snippet Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `title` | string | ✅ | Snippet title |
| `description` | string | ❌ | What it does |
| `code` | string | ✅ | The code itself |
| `tags` | array | ❌ | For searching/filtering |
| `language` | string | ❌ | Programming language |

---

## 📦 Complete Example

Here's a complete example for a "JavaScript Basics" topic:

### 1. Notes File (`data/notes/javascript.json`)

```json
{
  "metadata": {
    "category": "javascript",
    "title": "🟨 JavaScript Basics",
    "description": "Learn JavaScript fundamentals",
    "icon": "🟨",
    "difficulty": "beginner"
  },
  "topics": [
    {
      "id": 1,
      "title": "Variables in JavaScript",
      "icon": "📦",
      "content": "JavaScript has three ways to declare variables:\n\n• var - Function scoped (old way)\n• let - Block scoped, can be reassigned\n• const - Block scoped, cannot be reassigned\n\nBest practice: Use const by default, let when reassignment is needed, avoid var.",
      "key_points": [
        "let and const are block scoped",
        "var is function scoped",
        "const cannot be reassigned",
        "Always declare variables"
      ],
      "examples": [
        {
          "title": "Variable Declaration",
          "explanation": "Different ways to declare variables",
          "code": "const name = 'Alice';\nlet age = 25;\nvar oldWay = 'avoid';\n\nconsole.log(name); // Alice",
          "output": "Alice"
        }
      ]
    },
    {
      "id": 2,
      "title": "Functions",
      "icon": "⚡",
      "content": "Functions can be declared in multiple ways:\n\n• Function declaration\n• Function expression\n• Arrow function (ES6)\n\nArrow functions are concise and don't bind their own 'this'.",
      "key_points": [
        "Arrow functions use => syntax",
        "Regular functions have their own 'this'",
        "Arrow functions inherit 'this' from parent"
      ],
      "examples": [
        {
          "title": "Arrow Function",
          "explanation": "Modern function syntax",
          "code": "const add = (a, b) => a + b;\nconsole.log(add(2, 3));",
          "output": "5"
        }
      ]
    }
  ],
  "quizzes": [
    {
      "question": "Which keyword declares a block-scoped variable?",
      "options": ["var", "let", "const", "Both let and const"],
      "answer": 3,
      "explanation": "Both let and const are block-scoped. var is function-scoped."
    },
    {
      "question": "What is the output of: console.log(typeof null)?",
      "options": ["null", "undefined", "object", "number"],
      "answer": 2,
      "explanation": "Due to a historical bug, typeof null returns 'object'."
    }
  ],
  "code_snippets": [
    {
      "title": "Array Map",
      "description": "Transform array elements",
      "code": "const numbers = [1, 2, 3];\nconst doubled = numbers.map(n => n * 2);\nconsole.log(doubled); // [2, 4, 6]",
      "tags": ["array", "map", "functional"]
    }
  ]
}
```

### 2. Quiz File (`data/quizzes/javascript.json`)

```json
{
  "metadata": {
    "category": "javascript",
    "title": "🟨 JavaScript Quiz",
    "description": "Test your JS knowledge"
  },
  "questions": {
    "Variables": [
      {
        "q": "What is the scope of 'let' variables?",
        "options": [
          "Global only",
          "Function scope",
          "Block scope",
          "File scope"
        ],
        "answer": 2,
        "exp": "let variables are block-scoped, meaning they're only accessible within the {} block they're defined in."
      }
    ],
    "Functions": [
      {
        "q": "Which is NOT a valid function declaration?",
        "options": [
          "function foo() {}",
          "const foo = () => {}",
          "const foo = function() {}",
          "function := foo() {}"
        ],
        "answer": 3,
        "exp": "function := foo() {} is invalid syntax. The := operator doesn't exist in JavaScript."
      }
    ]
  }
}
```

---

## 📚 Adding Hierarchical Courses

Hierarchical courses provide a **6-level deep** learning path with **progression gating** — students can't advance until they meet requirements.

### Structure

```
Course → Category → Unit → Learning Outcome → Sub-topic → Content
```

### Create a Hierarchical JSON File

Save your course as `data/ksl/my_course.json`:

```json
{
  "metadata": {
    "title": "My Course Title",
    "author": "Your Name",
    "version": "1.0"
  },
  "courses": [
    {
      "id": "my_course_id",
      "code": "MC/101",
      "title": "My Course Title",
      "description": "What students will learn",
      "icon": "📘",
      "category": "my_category",
      "difficulty": "beginner",
      "estimated_minutes": 120,
      "credits": 2,
      "prerequisites": [],
      "tags": ["tag1", "tag2"],
      "learning_styles": ["visual", "hands-on", "reading"],
      "completion_requirements": {
        "min_score": 60,
        "must_complete_all": false
      },
      "instructor_notes": "Tips for teaching this course.",
      "glossary": [
        {"term": "Term1", "definition": "Definition here."}
      ],
      "media": [
        {
          "type": "video",
          "title": "Intro Video",
          "url": "https://example.com/video",
          "description": "What this video covers"
        }
      ],
      "resources": [
        {
          "name": "Cheat Sheet",
          "url": "https://example.com/cheatsheet.pdf",
          "description": "Quick reference"
        }
      ],
      "categories": [
        {
          "id": "cat_basics",
          "title": "Category Title",
          "description": "What this category covers",
          "estimated_minutes": 60,
          "difficulty": "beginner",
          "glossary": [],
          "case_studies": [
            {
              "title": "Case Study Title",
              "scenario": "Real-world scenario description.",
              "questions": ["Question 1?", "Question 2?"]
            }
          ],
          "discussion_prompts": [
            "Discussion question here?"
          ],
          "units": [
            {
              "id": "unit_1",
              "code": "MC/101/U1",
              "title": "Unit 1 Title",
              "description": "What this unit covers",
              "estimated_minutes": 30,
              "difficulty": "beginner",
              "prerequisites": [],
              "tools": ["Tool 1"],
              "equipment": ["Equipment 1"],
              "supplies": [],
              "instructor_notes": "Teaching tips.",
              "performance_standards": [
                "1.1 Standard description"
              ],
              "glossary": [],
              "case_studies": [],
              "media": [],
              "resources": [],
              "discussion_prompts": [],
              "completion_requirements": {},
              "learning_outcomes": [
                {
                  "id": "lo_1",
                  "title": "Learning Outcome 1",
                  "description": "What student will achieve",
                  "estimated_minutes": 15,
                  "min_score": 70,
                  "must_complete_all": false,
                  "difficulty": "beginner",
                  "discussion_prompts": [],
                  "case_studies": [],
                  "media": [],
                  "subtopics": [
                    {
                      "id": "sub_1",
                      "title": "Sub-topic Title",
                      "type": "content",
                      "estimated_minutes": 10,
                      "difficulty": "beginner",
                      "learning_styles": ["reading"],
                      "content": "Main content text here.",
                      "key_points": ["Point 1", "Point 2"],
                      "examples": [
                        {
                          "title": "Example Title",
                          "explanation": "How this works.",
                          "code": "code_example();"
                        }
                      ],
                      "media": [],
                      "resources": [],
                      "discussion_prompts": []
                    },
                    {
                      "id": "sub_quiz_1",
                      "title": "Quiz: Topic",
                      "type": "assessment",
                      "estimated_minutes": 5,
                      "difficulty": "beginner",
                      "content": "Test your knowledge.",
                      "quiz": [
                        {
                          "question": "What is the answer?",
                          "options": ["Option A", "Option B", "Option C", "Option D"],
                          "answer": 1,
                          "explanation": "Why B is correct."
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}
```

### Sub-topic Types

| Type | Purpose |
|------|---------|
| `content` | Main learning content |
| `example` | Illustrative examples |
| `activity` | Hands-on exercises |
| `assessment` | Quizzes (runs automatically when opened) |
| `reference` | Additional resources |

### Pack It Into a .ksl File

```bash
python ksl_tool.py pack data/ksl/my_course.json -t "My Course Title"
```

This creates `data/ksl/my_course.ksl` — the packaged format kslearn loads.

### Access Your Course

1. Launch: `kslearn`
2. Select **Option 1: Course Catalog**
3. Your course appears in the list
4. Navigate: Course → Category → Unit → Outcome → Sub-topic → Content

### Features Included

- ✅ **Progression gating** — students must pass previous levels
- ✅ **Mark as Complete** — `[X]` button on every sub-topic
- ✅ **Assessment quizzes** — embedded in `assessment` type sub-topics
- ✅ **Search & filter** — `[S]` search, `[F]` filter by difficulty
- ✅ **Continue where left off** — `[L]` returns to last-visited course
- ✅ **Reading time tracking** — tracks time spent in each topic
- ✅ **AI tutor** — `[A]` Ask AI about this course (offline/online)
- ✅ **AI suggestions** — proactively recommends "what to study next" after every interaction
- ✅ **Enrichment fields** — glossary, case studies, media, resources, discussions

### Tips for AI Suggestions

To make AI suggestions more relevant for your courses:

1. **Add descriptive tags** — The suggestion engine matches courses by shared tags
2. **Set accurate difficulty** — Helps the engine suggest appropriate next steps
3. **Include quiz assessments** — Quiz scores drive weak-area recommendations
4. **Use consistent categories** — Courses in the same category are cross-suggested

---

## ✅ Testing Your Content

### Step 1: Validate JSON

Before testing, validate your JSON syntax:

```bash
# Using Python
python -m json.tool data/notes/your_topic.json > /dev/null && echo "Valid JSON"

# Or use an online validator like jsonlint.com
```

### Step 2: Test in kslearn

1. **Launch kslearn:**
   ```bash
   kslearn
   ```

2. **Test Notes:**
   - Select **Option 1: Study Notes**
   - Find your new topic in the list
   - Navigate through topics
   - Check formatting displays correctly

3. **Test Quiz:**
   - Select **Option 2: Take Quiz**
   - Find your quiz
   - Answer questions
   - Verify correct answers and explanations

4. **Test Snippets:**
   - While viewing a topic, press **S**
   - Check code displays correctly

### Step 3: Check Progress Tracking

After completing a quiz:
- Go to **Option 4: My Progress**
- Verify your quiz is recorded
- Check score is saved correctly

---

## 💡 Tips & Best Practices

### Content Quality

✅ **DO:**
- Write clear, concise explanations
- Use examples for every concept
- Include real-world use cases
- Add multiple choice questions with good distractors
- Write helpful explanations for quiz answers
- Use consistent formatting
- Test all code examples

❌ **DON'T:**
- Write walls of text (break into paragraphs)
- Use ambiguous quiz questions
- Make all quiz answers obviously wrong except one
- Include code that doesn't run
- Forget to proofread

### JSON Formatting

✅ **DO:**
- Use 2-space indentation
- Keep lines under 80 characters when possible
- Escape special characters properly
- Use meaningful category names
- Include version in metadata

❌ **DON'T:**
- Mix tabs and spaces
- Forget commas between array/object items
- Use single quotes (JSON requires double quotes)
- Leave trailing commas

### Quiz Design

✅ **Good Question:**
```json
{
  "q": "What is the output of print(2 ** 3)?",
  "options": ["6", "8", "9", "Error"],
  "answer": 1,
  "exp": "2 ** 3 means 2 to the power of 3, which equals 8."
}
```

❌ **Bad Question:**
```json
{
  "q": "What does this do?",
  "options": ["A", "B", "C", "D"],
  "answer": 0,
  "exp": "Because it does A."
}
```

### Icons & Emojis

Use relevant emojis for visual organization:

| Category | Suggested Icons |
|----------|----------------|
| Python | 🐍 |
| JavaScript | 🟨 |
| AI/ML | 🤖 |
| Web Dev | 🌐 |
| Security | 🔒 |
| Linux | 🐧 |
| Database | 🗄️ |
| Git | 📦 |

### File Naming

- Use lowercase with underscores: `your_topic.json`
- Match filename to category: `javascript.json` for category "javascript"
- Be consistent across notes/quizzes/snippets

---

## 🔧 Troubleshooting

### Content Not Showing Up

**Problem:** New topic doesn't appear in menu

**Solutions:**
1. Check JSON syntax: `python -m json.tool data/notes/your_topic.json`
2. Verify file is in correct directory
3. Check `metadata.category` matches filename
4. Restart kslearn (changes aren't hot-reloaded)

### Quiz Not Loading

**Problem:** Quiz shows "No questions found"

**Solutions:**
1. Ensure `questions` key exists in JSON
2. Check question format (q, options, answer, exp)
3. Verify `answer` is a number (0-3), not string
4. Make sure options array has 4 items

### Formatting Issues

**Problem:** Text displays incorrectly

**Solutions:**
1. Use `\n` for line breaks, not actual newlines in strings
2. Escape quotes: `\"` instead of `"`
3. Use bullet points: `•`
4. Keep content strings under 1000 characters per topic

---

## 📚 Quick Reference

### Minimal Notes File
```json
{
  "metadata": {
    "category": "topic",
    "title": "📖 Topic Name",
    "description": "Description"
  },
  "topics": [
    {
      "id": 1,
      "title": "First Topic",
      "content": "Content here"
    }
  ],
  "quizzes": [],
  "code_snippets": []
}
```

### Minimal Quiz File
```json
{
  "metadata": {
    "category": "topic",
    "title": "Quiz Name"
  },
  "questions": {
    "Topic": [
      {
        "q": "Question?",
        "options": ["A", "B", "C", "D"],
        "answer": 0,
        "exp": "Explanation"
      }
    ]
  }
}
```

### Minimal Snippets File
```json
{
  "metadata": {
    "category": "topic",
    "title": "Snippets"
  },
  "snippets": [
    {
      "title": "Example",
      "code": "print('Hello')"
    }
  ]
}
```

---

## 🎉 Summary

Adding new content to kslearn is easy:

1. **Create JSON files** in `data/notes/`, `data/quizzes/`, `data/snippets/`
2. **Follow the format** shown in examples
3. **Validate JSON** syntax before testing
4. **Test in kslearn** to ensure everything works
5. **Share your content** with the community!

For examples, check existing files in the `data/` directory or visit the [kslearn GitHub](https://github.com/kashsight/kslearn).

---

**Happy Teaching! 📚✨**

*Made with ❤️ for educators and learners everywhere*
