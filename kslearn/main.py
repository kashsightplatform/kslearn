#!/usr/bin/env python3
"""kslearn Main Launcher - Legacy compatibility mode"""

import os
import sys
import time
import random
import threading

# Try to import rich UI, fall back to ANSI colors if not available
try:
    from kslearn.ui import (
        console,
        get_banner,
        get_small_banner,
        show_panel,
        show_success,
        show_error,
        show_warning,
        show_info,
        LoadingSpinner,
        create_study_grid,
        print_divider,
    )
    USE_RICH = True
except ImportError:
    USE_RICH = False

# ANSI Colors (fallback)
class Colors:
    RED = "\033[31m"
    GREEN = "\033[32m"
    ORANGE = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    BLACK = "\033[30m"
    YELLOW = "\033[93m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

def clear_screen():
    """Cross-platform screen clear — works on Windows, Linux, macOS, Termux."""
    import sys
    import os
    try:
        # Windows
        if os.name == "nt":
            os.system("cls")
        # Unix-like (Linux, macOS, Termux, Android)
        else:
            os.system("clear")
    except Exception:
        # Fallback: print ANSI escape sequence
        print("\033[2J\033[H", end="")

def banner():
    if USE_RICH:
        console.print(get_banner())
    else:
        print(f"""{Colors.CYAN}
    ╔══════════════════════════════════════════════════════╗
    ║   ███╗   ██╗███████╗██╗    ██╗███████╗               ║
    ║   ████╗  ██║██╔════╝██║    ██║██╔════╝               ║
    ║   ██╔██╗ ██║█████╗  ██║ █╗ ██║███████╗               ║
    ║   ██║╚██╗██║██╔══╝  ██║███╗██║╚════██║               ║
    ║   ██║ ╚████║███████╗╚███╔███╔╝███████║               ║
    ║   ╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝ ╚══════╝               ║
    ║                                                      ║
    ║        ██████╗ ███████╗██╗     ███████╗              ║
    ║        ██╔══██╗██╔════╝██║     ██╔════╝              ║
    ║        ██████╔╝█████╗  ██║     █████╗                ║
    ║        ██╔══██╗██╔══╝  ██║     ██╔══╝                ║
    ║        ██║  ██║███████╗███████╗███████╗              ║
    ║        ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝              ║
    ║                                                      ║
    ║     {Colors.GREEN}📚 Learn Anything - Math, Science & More{Colors.CYAN}        ║
    ║     {Colors.YELLOW}🎮 v1.0.0 - JSON-Powered Education{Colors.CYAN}             ║
    ║     {Colors.CYAN}🚀 Works on: Termux • Linux • macOS • Windows{Colors.WHITE}    ║
    ╚══════════════════════════════════════════════════════╝
    """)

def banner_small():
    if USE_RICH:
        console.print(get_small_banner())
    else:
        print(f"""{Colors.CYAN}
    ╔═══════════════════════════════════════╗
    ║     {Colors.BOLD}{Colors.YELLOW}KSLEARN{Colors.RESET}{Colors.CYAN} v1.0.0                  ║
    ╚═══════════════════════════════════════╝{Colors.WHITE}
    """)

def loading(message, duration=1.5):
    if USE_RICH:
        with LoadingSpinner(message):
            time.sleep(duration)
    else:
        spin = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
        print(f"{Colors.GREEN}[{Colors.WHITE}+{Colors.GREEN}]{Colors.CYAN} {message} ", end="", flush=True)
        for i in range(int(duration * 10)):
            print(f"\r{Colors.GREEN}[{Colors.WHITE}+{Colors.GREEN}]{Colors.CYAN} {message} {spin[i % 10]}", end="", flush=True)
            time.sleep(0.1)
        print(f"\r{Colors.GREEN}[{Colors.WHITE}✓{Colors.GREEN}]{Colors.GREEN} {message} - Done!{Colors.WHITE}    ")

def show_status(status, message):
    if USE_RICH:
        if status == "success":
            show_success(message)
        elif status == "error":
            show_error(message)
        elif status == "warning":
            show_warning(message)
        elif status == "info":
            show_info(message)
    else:
        if status == "success":
            print(f"{Colors.GREEN}[{Colors.WHITE}✓{Colors.GREEN}]{Colors.GREEN} {message}{Colors.WHITE}")
        elif status == "error":
            print(f"{Colors.RED}[{Colors.WHITE}✗{Colors.RED}]{Colors.RED} {message}{Colors.WHITE}")
        elif status == "warning":
            print(f"{Colors.ORANGE}[{Colors.WHITE}!{Colors.ORANGE}]{Colors.ORANGE} {message}{Colors.WHITE}")
        elif status == "info":
            print(f"{Colors.BLUE}[{Colors.WHITE}i{Colors.BLUE}]{Colors.CYAN} {message}{Colors.WHITE}")

def grid_menu(title, options, cols=2):
    if USE_RICH:
        console.clear()
        console.print(get_small_banner())
        console.print()
        show_panel(title, "Choose an activity to start learning!\n", "cyan")
        
        table = create_study_grid(options) if USE_RICH else None
        if table:
            console.print(table)
    else:
        clear_screen()
        banner_small()
        print()
        print(f"{Colors.RED}[{Colors.WHITE}::{Colors.RED}]{Colors.ORANGE} {title} {Colors.RED}[{Colors.WHITE}::{Colors.RED}]{Colors.ORANGE}")
        print()

        count = 1
        for option in options:
            print(f"{Colors.RED}[{Colors.WHITE}{count:02d}{Colors.RED}]{Colors.ORANGE} {option:<25}", end="")
            if count % cols == 0:
                print()
            count += 1

        if count % cols != 1:
            print()

    print(f"\n{Colors.RED}[{Colors.WHITE}00{Colors.RED}]{Colors.ORANGE} Exit{Colors.WHITE}")
    print()

def about():
    if USE_RICH:
        console.clear()
        console.print(get_banner())
        console.print()
        show_panel("About kslearn", """
Version:     1.0.0
Author:      KashSight Platform
License:     MIT

Learn Anything:
• General Education - Math, Science, Computer Literacy
• Technology - Programming, Web Dev, Linux, DevOps
• AI & Data Science - ML, Neural Networks, Statistics
• Cybersecurity - Malware, Networks, Cryptography
• Humanities - Psychology, History, Religion, Languages
• Arts & Life - Music, Art, Business, Health
• And anything else you want to learn!

New Features:
• 📚 Learning Notes - Study materials with quizzes
• ⏰ Smart Reminders - Random quiz after 3 mins
• ❤️  Support - Donate and follow on social media

Support kslearn:
• GitHub: https://github.com/kashsight/kslearn
• Donate: https://ko-fi.com/kslearn
""", "cyan")
    else:
        clear_screen()
        banner()
        print(f"""
    {Colors.CYAN}About kslearn{Colors.WHITE}

    {Colors.GREEN}Version:{Colors.WHITE}     1.0.0
    {Colors.GREEN}Author:{Colors.WHITE}      KashSight Platform
    {Colors.GREEN}License:{Colors.WHITE}     MIT

    {Colors.CYAN}Description:{Colors.WHITE}
    A general learning platform — study math, science,
    psychology, religion, music, technology, and anything else!

    {Colors.CYAN}Learning Tracks:{Colors.WHITE}
    • General Education - Math, Science, Computer Literacy
    • Technology - Programming, Web Dev, Linux, DevOps
    • AI & Data Science - ML, Neural Networks, Statistics
    • Cybersecurity - Malware, Networks, Cryptography
    • Humanities - Psychology, History, Religion, Languages
    • Arts & Life - Music, Art, Business, Health
    • General Knowledge - Geography, History, Sports

    {Colors.CYAN}New Features:{Colors.WHITE}
    • 📚 Learning Notes - Study materials with quizzes
    • ⏰ Smart Reminders - Random quiz after 3 mins
    • ❤️  Support - Donate and follow on social media

    {Colors.CYAN}Controls:{Colors.WHITE}
    • Number Keys - Select options
    • Enter - Confirm selection
    • Q - Quit current game
    • Cross-platform: PC, Mac, Linux, Termux

    {Colors.CYAN}Support kslearn:{Colors.WHITE}
    • GitHub: https://github.com/kashsight/kslearn
    • Donate: https://ko-fi.com/kslearn
    """)
    input(f"{Colors.GREEN}Press Enter to continue...{Colors.WHITE}")

# Global timer state
class TimerState:
    def __init__(self):
        self.start_time = None
        self.quiz_triggered = False
        self.running = True

timer_state = TimerState()

def start_learning_timer():
    """Start a timer that triggers a random quiz after 3 minutes"""
    def timer_thread():
        time.sleep(180)  # 3 minutes = 180 seconds
        if timer_state.running and not timer_state.quiz_triggered:
            timer_state.quiz_triggered = True
            trigger_random_quiz()

    thread = threading.Thread(target=timer_thread, daemon=True)
    thread.start()

def trigger_random_quiz():
    """Trigger a random learning quiz"""
    if USE_RICH:
        console.clear()
        console.print(Panel(
            "[bold yellow]⏰ TIME FOR A QUIZ![/bold yellow]\n\n"
            "[white]You've been learning for 3 minutes!\n"
            "Time for a quick knowledge check![/white]\n\n"
            "[cyan]This will help reinforce what you've learned.[/cyan]",
            box="ROUNDED",
            border_style="yellow",
        ))
    else:
        clear_screen()
        print(f"""{Colors.CYAN}
    ╔═══════════════════════════════════════╗
    ║     {Colors.BOLD}⏰ TIME FOR A QUIZ!{Colors.RESET}{Colors.CYAN}          ║
    ╚═══════════════════════════════════════╝{Colors.WHITE}
    """)
        print(f"""
  {Colors.YELLOW}You've been learning for 3 minutes!{Colors.WHITE}
  {Colors.CYAN}Time for a quick knowledge check!{Colors.WHITE}

  {Colors.GREEN}This will help reinforce what you've learned.{Colors.WHITE}

  {Colors.YELLOW}Quick Quiz Topics:{Colors.WHITE}
  • Python Programming
  • AI & Machine Learning
  • Cybersecurity
  • Web Development
""")

    choice = input(f"\n  {Colors.GREEN}Start quiz? (y/n):{Colors.WHITE} ").strip().lower()

    if choice == "y":
        run_random_quiz()

    timer_state.quiz_triggered = False

def run_random_quiz():
    """Run a random quiz from learning notes"""
    try:
        from kslearn.main.learning_notes import LEARNING_NOTES

        topics = list(LEARNING_NOTES.keys())
        topic_key = random.choice(topics)
        topic = LEARNING_NOTES[topic_key]
        quizzes = topic["quizzes"]

        if not quizzes:
            show_status("warning", "No quizzes available!")
            time.sleep(2)
            return

        # Pick 3 random questions
        quiz_questions = random.sample(quizzes, min(3, len(quizzes)))
        score = 0

        if USE_RICH:
            from rich.panel import Panel
            from rich import box
            console.clear()
            console.print(Panel(
                f"[bold cyan]📝 QUICK QUIZ: {topic['title']}[/bold cyan]",
                box=box.ROUNDED,
                border_style="cyan",
            ))
        else:
            clear_screen()
            print(f"""{Colors.CYAN}
    ╔═══════════════════════════════════════╗
    ║     {Colors.BOLD}📝 QUICK QUIZ: {topic["title"]}{Colors.RESET}{Colors.CYAN} ║
    ╚═══════════════════════════════════════╝{Colors.WHITE}
    """)

        for i, quiz in enumerate(quiz_questions, 1):
            print(f"\n  {Colors.CYAN}Question {i}/{len(quiz_questions)}{Colors.WHITE}")
            print(f"  {Colors.YELLOW}{'─' * 40}{Colors.WHITE}")
            print(f"\n  {quiz['question']}\n")

            for j, option in enumerate(quiz["options"]):
                print(f"  {Colors.GREEN}[{Colors.WHITE}{j+1}{Colors.GREEN}]{Colors.WHITE} {option}")

            print()

            while True:
                try:
                    answer = input(f"  {Colors.YELLOW}Your answer:{Colors.WHITE} ").strip()
                    answer_num = int(answer)
                    if 1 <= answer_num <= 4:
                        break
                    print(f"  {Colors.RED}Please enter 1-4{Colors.WHITE}")
                except ValueError:
                    print(f"  {Colors.RED}Please enter a number{Colors.WHITE}")

            if answer_num == quiz["answer"] + 1:
                score += 1
                print(f"\n  {Colors.GREEN}✓ Correct!{Colors.WHITE}")
            else:
                print(f"\n  {Colors.RED}✗ Wrong!{Colors.WHITE}")
                print(f"  {Colors.CYAN}Answer: {quiz['explanation']}{Colors.WHITE}")

            print()

        # Show results
        percentage = (score / len(quiz_questions)) * 100
        print(f"  {Colors.YELLOW}{'─' * 40}{Colors.WHITE}")
        print(f"  {Colors.YELLOW}Score:{Colors.WHITE} {score}/{len(quiz_questions)} ({percentage:.0f}%)")

        if percentage >= 70:
            print(f"  {Colors.GREEN}🎉 Great job!{Colors.WHITE}")
        else:
            print(f"  {Colors.CYAN}📚 Keep learning!{Colors.WHITE}")

        print()
        input(f"  {Colors.GREEN}Press Enter to continue...{Colors.WHITE}")

    except Exception as e:
        show_status("error", f"Quiz error: {e}")
        time.sleep(2)

def run_learning_notes():
    """Run the learning notes module"""
    try:
        module = __import__("kslearn.main.learning_notes", fromlist=[""])
        if hasattr(module, "main"):
            module.main()
        # Reset timer after viewing notes
        timer_state.quiz_triggered = False
    except Exception as e:
        show_status("error", f"Failed to load learning notes: {e}")
        time.sleep(2)

def run_support():
    """Run the support/donation module"""
    try:
        module = __import__("kslearn.main.support", fromlist=[""])
        if hasattr(module, "main"):
            module.main()
    except Exception as e:
        show_status("error", f"Failed to load support menu: {e}")
        time.sleep(2)

def run_game(game_name):
    """Import and run a game module"""
    try:
        module = __import__(f"kslearn.main.{game_name}", fromlist=[""])
        if hasattr(module, "main"):
            module.main()
        elif hasattr(module, "play"):
            module.play()
    except Exception as e:
        show_status("error", f"Failed to run game: {e}")
        time.sleep(2)

def main_menu():
    games = [
        "Programming Quiz",
        "Coding Challenge",
        "Tech Trivia",
        "Math Challenge",
        "Science Quiz",
        "Web Dev Quiz",
        "AI/ML Quiz",
        "Cybersecurity Quiz",
        "Computer Literacy",
        "General Knowledge",
    ]

    extra_options = [
        "📚 Learning Notes",
        "❤️  Support kslearn",
    ]

    all_options = games + extra_options

    grid_menu("Select Study Mode", all_options)
    choice = input().strip()

    if choice == "0" or choice == "00":
        show_status("info", "Thanks for learning! Goodbye!")
        sys.exit(0)
    elif choice == "99":
        about()
        return
    elif choice == "11":
        run_learning_notes()
        return
    elif choice == "12":
        run_support()
        return

    try:
        choice_num = int(choice)
        if 1 <= choice_num <= len(games):
            game_map = {
                1: "programming_quiz",
                2: "coding_challenge",
                3: "tech_trivia",
                4: "math_challenge",
                5: "science_quiz",
                6: "web_dev_quiz",
                7: "ai_ml_quiz",
                8: "cybersecurity_quiz",
                9: "computer_literacy",
                10: "general_knowledge",
            }
            game = game_map.get(choice_num)
            if game:
                clear_screen()
                loading(f"Loading {games[choice_num-1]}...")
                run_game(game)
                # Return to main menu after game
                return
        else:
            show_status("warning", "Invalid option!")
            time.sleep(1)
    except ValueError:
        show_status("warning", "Please enter a number!")
        time.sleep(1)

def main():
    clear_screen()
    banner()
    loading("Initializing kslearn")
    time.sleep(0.5)

    # Start the learning timer for random quizzes
    start_learning_timer()

    while True:
        main_menu()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.RED}[{Colors.WHITE}!{Colors.RED}]{Colors.RED} Game Interrupted.{Colors.WHITE}")
        sys.exit(0)
