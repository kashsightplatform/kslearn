# kslearn UI Design Specification

> **Canonical reference** for all UI patterns, colors, components, and conventions used across the kslearn codebase.
> All developers MUST follow this document to maintain UI consistency.

---

## 1. Technology Stack

| Layer | Library | Purpose |
|-------|---------|---------|
| CLI Framework | **Click** (`click>=8.0.0`) | Command routing, argument parsing |
| Terminal UI | **Rich** (`rich>=12.0.0`) | All terminal formatting, panels, tables |
| Console | `rich.console.Console` | Single shared console instance |

**No HTML, CSS, or web frameworks.** This is a pure terminal application.

---

## 2. Color Palette

### 2.1 Canonical Colors (defined in `kslearn/ui.py`)

```python
COLORS = {
    "primary":   "cyan",        # Default content, headers, borders
    "secondary": "green",       # Success, free content, confirmations
    "accent":    "yellow",      # Warnings, numbering, hints
    "danger":    "red",         # Errors, incorrect answers, hard mode
    "info":      "blue",        # Informational messages, links
    "success":   "bright_green",# Streaks, achievements
    "warning":   "orange1",     # Cautions, hints
    "muted":     "dim white",   # Descriptions, secondary text
}
```

### 2.2 Semantic Color Mapping

| Context | Color | Usage |
|---------|-------|-------|
| Default panels | `cyan` | Content panels, menus, headers |
| Success | `green` | Correct answers, saved confirmations |
| Warning | `yellow` | Hints, cautions, achievements |
| Error | `red` | Wrong answers, invalid input |
| Info | `blue` | Social media, links, help |
| Premium | `magenta` | Premium content, bookmarks |
| Streaks | `bright_yellow` | Streak notifications |
| Descriptions | `dim white` | Subtitles, secondary info |

### 2.3 Border Style by Component

| Component | Border Style | Box Style |
|-----------|-------------|-----------|
| Content panels | `cyan` | `ROUNDED` |
| Success messages | `green` | `ROUNDED` |
| Warning panels | `yellow` | `ROUNDED` |
| Error panels | `red` | `ROUNDED` |
| Code blocks | `green` | `ASCII` |
| Links display | `blue` | `ASCII` |
| Main banner | `bright_cyan` | `DOUBLE` |
| Achievements | `bright_yellow` | `DOUBLE` |
| Daily challenges | `bright_cyan` | `DOUBLE` |

---

## 3. Typography & Text Formatting

### 3.1 Rich Markup Patterns

```python
# Bold colored text (headers, titles)
"[bold cyan]Title[/bold cyan]"
"[bold green]Success[/bold green]"
"[bold red]Error[/bold red]"

# Dim text (descriptions, subtitles)
"[dim]Description text[/dim]"

# Colored body text
"[cyan]Content[/cyan]"
"[white]Important text[/white]"
"[yellow]Warning text[/yellow]"

# Links
"[blue underline]https://example.com[/blue underline]"

# Icons
"[bold green]✓[/bold green]"   # Success checkmark
"[bold red]✗[/bold red]"       # Error X
"[bold yellow]![/bold yellow]"  # Warning exclamation
"[bold blue]●[/bold blue]"      # Info bullet
```

### 3.2 Emoji Prefix Convention

Every section header MUST have a leading emoji:

| Emoji | Section |
|-------|---------|
| 📚 | Study Notes, Learning |
| 📝 | Quizzes, Quiz Results |
| 🤖 | AI Chat |
| 📊 | Progress, Statistics |
| 🔖 | Bookmarks |
| 🧠 | Knowledge Brain |
| 🏪 | Data Store |
| ❤️ | Support, Donations |
| ⚙️ | Settings |
| ❓ | Help |
| ❌ | Exit |
| 🔥 | Streaks |
| ⭐ | Achievements |
| 💡 | Hints, Tips |
| 📥 | Downloads |
| 💝 | Donations |
| 📢 | Social Media |
| 🔑 | Key Concepts, API Keys |
| 🎯 | Goals, Impact |
| 📜 | Credits |
| 📋 | Links List |
| 🔗 | Open Links |
| 📦 | Bundles, ZIP |
| 🎲 | Random |

---

## 4. Component Library

All components are defined in `kslearn/ui.py` and MUST be imported from there.
**No duplicate component definitions in other files.**

### 4.1 Panels

```python
# Standard content panel
Panel(
    content,                                    # Text or Text.assemble()
    title=f"[bold {style}]{title}[/bold {style}]",
    border_style=style,                        # Default: "cyan"
    box=box.ROUNDED,
)

# Panel with padding
Panel(
    content,
    box=box.ROUNDED,
    border_style="cyan",
    padding=(1, 2),
)

# Panel with title alignment
Panel(
    content,
    box=box.ROUNDED,
    border_style="cyan",
    title="📚 Title",
    title_align="left",
)
```

### 4.2 Tables

```python
# Standard menu table
table = Table(
    box=box.ROUNDED,
    border_style="cyan",
    show_header=False,
    expand=True,
)
table.add_column("Option", style="bold white", ratio=1)
table.add_column("Description", style="dim", ratio=2)

# Table with headers
table = Table(
    box=box.ROUNDED,
    border_style="cyan",
    show_header=True,
)
table.add_column("#", style="yellow", width=4, justify="center")
table.add_column("Name", style="bold white")
table.add_column("Description", style="dim")
```

### 4.3 Dividers

```python
# Use the canonical print_divider() from ui.py
from kslearn.ui import print_divider

print_divider()                 # Simple line
print_divider("Section", "dim") # Labeled divider
```

### 4.4 Rules (horizontal lines)

```python
from rich.rule import Rule

console.print(Rule("[dim]Navigation[/dim]", style="cyan"))
```

---

## 5. Input Prompts

### 5.1 Standard Prompt Style

ALL interactive prompts MUST use this exact format:

```python
# Standard unicode arrow prompt
console.input("[bold green]╰─► Your choice:[/bold green] ")

# With specific label
console.input("[bold green]╰─► Select topic:[/bold green] ")
console.input("[bold green]╰─► Your answer:[/bold green] ")
console.input("[bold green]╰─► Press Enter to continue...[/bold green] ")
```

### 5.2 Prompt Variants

```python
# Confirmation prompt
console.input("[bold green]Question?[/bold green] [Y/n]: ")

# Text input with hint
console.input("[bold green]Enter value:[/bold green] [dim](default: 5)[/dim]: ")
```

### 5.3 Numbered Option Lists

```python
# Standard numbered options
for i, option in enumerate(options, 1):
    console.print(f"  [yellow]{i:02d}[/yellow] [white]{option}[/white]")

# With description
for i, (name, desc) in enumerate(options, 1):
    console.print(f"  [yellow]{i:02d}[/yellow] [white]{name}[/white] [dim]({desc})[/dim]")

# With 0 = Back option
console.print(f"  [yellow] 0[/yellow] [white]Back[/white]")
```

---

## 6. Status Messages

Use the canonical functions from `ui.py`:

```python
from kslearn.ui import show_success, show_error, show_warning, show_info

show_success("File saved successfully!")
show_error("Failed to load quiz data.")
show_warning("This action cannot be undone.")
show_info("Use 'kslearn study' to browse notes.")
```

**Output format:**
- Success: `✓ message` (green)
- Error: `✗ message` (red)
- Warning: `! message` (yellow)
- Info: `● message` (blue)

---

## 7. Screen Management

### 7.1 Clear Screen

Use ONLY the canonical `clear_screen()` from `ui.py`:

```python
from kslearn.ui import clear_screen

clear_screen()
```

**Implementation** (defined once in `ui.py`):
```python
def clear_screen():
    """Clear terminal screen - works on Termux and all platforms"""
    print("\033[2J\033[H", end="")
    console.file.flush()
```

**DO NOT** define `clear_screen()` in any other file.

---

## 8. Console Instance

### 8.1 Single Shared Console

There is exactly ONE `Console` instance, defined in `kslearn/ui.py`:

```python
# In kslearn/ui.py
from rich.console import Console
console = Console()
```

All other files MUST import and use this shared instance:

```python
from kslearn.ui import console

console.print("...")
console.input("...")
```

**DO NOT** create `console = Console()` in any other file.

---

## 9. Layout Conventions

### 9.1 Standard Screen Flow

Every screen follows this pattern:

```
1. clear_screen()
2. console.print(banner or header panel)
3. console.print()                         # Blank line
4. console.print(content panel/table)      # Main content
5. console.print()                         # Blank line
6. console.print(actions/navigation table) # Options
7. console.print()                         # Blank line
8. choice = console.input("[bold green]╰─► ...[/bold green] ")
```

### 9.2 Panel Spacing

- Always print a blank `console.print()` before and after panels
- Tables should have a blank line above and below

### 9.3 Navigation Patterns

```python
# Standard navigation table (no box, compact)
nav_table = Table(
    box=None,
    show_header=False,
    expand=True,
    padding=(0, 1),
)
nav_table.add_column("Key", style="green")
nav_table.add_column("Action", style="white")

nav_table.add_row("[N]", "Next Topic")
nav_table.add_row("[P]", "Previous Topic")
nav_table.add_row("[Q]", "Take Quiz")
nav_table.add_row("[A]", "Ask AI")
nav_table.add_row("[B]", "Bookmark This Topic")
nav_table.add_row("[0]", "Back to Topics")
```

---

## 10. File Organization

### 10.1 UI Component Ownership

| File | Responsibility |
|------|---------------|
| `kslearn/ui.py` | **All** UI components, colors, prompts, panels, tables, status messages, clear_screen |
| `kslearn/cli.py` | Main menu, command routing, interactive flow |
| `kslearn/engines/quiz_engine.py` | Quiz-specific UI (uses ui.py components) |
| `kslearn/engines/notes_viewer.py` | Notes-specific UI (uses ui.py components) |
| `kslearn/main/ai_chat.py` | Chat UI (uses ui.py components) |
| `kslearn/main/datastore.py` | Store UI (uses ui.py components) |
| `kslearn/main/support.py` | Support UI (uses ui.py components) |

### 10.2 Import Pattern

Every file that produces UI output MUST import from `ui.py`:

```python
from kslearn.ui import (
    console,
    show_panel,
    show_success,
    show_error,
    show_warning,
    show_info,
    print_divider,
    clear_screen,
    LoadingSpinner,
)
```

---

## 11. Box Styles Reference

| Box Style | Import | Usage |
|-----------|--------|-------|
| `box.ROUNDED` | `from rich import box` | Default for all panels |
| `box.ASCII` | `from rich import box` | Code blocks, link displays |
| `box.DOUBLE` | `from rich import box` | Main banner, achievements, daily challenges |

```python
from rich import box
# or
from rich.box import ROUNDED, ASCII, DOUBLE
```

---

## 12. Loading & Progress Indicators

### 12.1 Loading Spinner

```python
from kslearn.ui import LoadingSpinner

with LoadingSpinner("Loading content..."):
    time.sleep(0.5)  # Simulate work
```

### 12.2 Progress Bar

```python
from kslearn.ui import create_progress

progress = create_progress()
with progress:
    task = progress.add_task("Loading...", total=100)
    # ... work ...
    progress.update(task, advance=50)
```

---

## 13. Achievement & Notification Patterns

### 13.1 Achievement

```python
from kslearn.ui import show_achievement

show_achievement("Perfect Score", "Answered all questions correctly", "🏆")
```

### 13.2 Hint

```python
from kslearn.ui import show_hint

show_hint("The answer relates to Python decorators", 3)
```

### 13.3 Streak

```python
from kslearn.ui import show_streak

show_streak(7)  # Shows "⭐ On a roll! [7x streak bonus!]"
```

---

## 14. Anti-Patterns (DO NOT DO THESE)

1. **DO NOT** create `console = Console()` outside of `ui.py`
2. **DO NOT** define `clear_screen()` outside of `ui.py`
3. **DO NOT** define `print_divider()` outside of `ui.py`
4. **DO NOT** hardcode color literals — use `COLORS` dict or documented semantic colors
5. **DO NOT** mix prompt styles — always use `╰─►` unicode arrow
6. **DO NOT** use raw ANSI escape codes for colors (use Rich markup)
7. **DO NOT** create duplicate panel/table helper functions in other files
8. **DO NOT** use `input()` — always use `console.input()`
9. **DO NOT** use `print()` — always use `console.print()`

---

## 15. Theme Configuration

The file `data/config/theme.json` defines color schemes for future use:
- `cyan` (default), `blue`, `green`, `purple`, `orange`

Currently, colors are hardcoded via the `COLORS` dict in `ui.py`.
The theme.json file is reserved for future theme-switching functionality.

---

## 16. Version

| Property | Value |
|----------|-------|
| Document Version | 1.0.0 |
| kslearn Version | 1.0.0 |
| Last Updated | 2026-04-03 |
| Author | kslearn Team |
