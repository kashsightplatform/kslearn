# 🚀 kslearn Installation Guide

Complete installation instructions for all platforms - from scratch to fully working!

---

## 📋 Table of Contents

1. [Quick Start](#quick-start)
2. [Android (Termux)](#android-termux)
3. [Linux (Ubuntu/Debian)](#linux-ubuntudebian)
4. [macOS](#macos)
5. [Windows](#windows)
6. [Installation Methods](#installation-methods)
7. [Verification](#verification)
8. [Troubleshooting](#troubleshooting)
9. [Uninstallation](#uninstallation)

---

## ⚡ Quick Start

**Already have Python? Install in 30 seconds:**

```bash
# Method 1: Git Clone (Recommended)
git clone https://github.com/kashsightplatform/kslearn.git
cd kslearn
pip install -e .
kslearn

# v1.1.0 — 13 streamlined features, AI-powered suggestions, hierarchical courses
```

# Method 2: ZIP Download
# Download from GitHub → Code → Download ZIP
# Extract and run:
cd kslearn
pip install -e .

# Start learning!
kslearn
```

---

## 📱 Android (Termux)

### Prerequisites

- Android device
- Termux app (from F-Droid recommended, or Play Store)

### Step-by-Step Installation

#### 1. Update Termux Packages

```bash
pkg update && pkg upgrade -y
```

#### 2. Install Python

```bash
pkg install python -y
```

#### 3. Install Required Dependencies

```bash
pkg install python-pip -y
pkg install git -y
pkg install build-essential -y
```

#### 4. Install kslearn

**Option A: Git Clone (Recommended)**

```bash
git clone https://github.com/kashsightplatform/kslearn.git
cd kslearn
pip install -e .
```

**Option B: ZIP Download**

1. Open browser in Termux:
   ```bash
   pkg install wget -y
   ```

2. Download ZIP:
   ```bash
   wget https://github.com/kashsightplatform/kslearn/archive/refs/heads/main.zip
   ```

3. Install unzip and extract:
   ```bash
   pkg install unzip -y
   unzip main.zip
   cd kslearn-main
   pip install -e .
   ```

#### 5. (Optional) Install AI Chat - tgpt

For offline AI chat feature:

```bash
# Install termux-ai for AI chat
pkg install termux-ai -y

# Or install tgpt directly
curl -sL https://is.gd/Termux_Ai | bash
```

#### 6. Verify Installation

```bash
kslearn --version
```

#### 7. Launch kslearn

```bash
kslearn
```

Or use the shortcut:
```bash
ksl
```

### Termux Quick Install (One-Liner)

```bash
pkg update && pkg upgrade -y && pkg install python git -y && git clone https://github.com/kashsightplatform/kslearn.git && cd kslearn && pip install -e . && kslearn
```

### Termux Troubleshooting

**Problem:** `pip` not found
```bash
pkg install python-pip -y
```

**Problem:** Permission denied
```bash
chmod +x setup.py
pip install --user -e .
```

**Problem:** Installation fails
```bash
pip install --upgrade pip
pip install -e . --no-cache-dir
```

---

## 🐧 Linux (Ubuntu/Debian)

### Prerequisites

- Ubuntu 20.04+ / Debian 10+ / Linux Mint 20+
- Terminal access

### Step-by-Step Installation

#### 1. Update System Packages

```bash
sudo apt update && sudo apt upgrade -y
```

#### 2. Install Python and pip

```bash
sudo apt install python3 python3-pip python3-venv -y
```

#### 3. Install Git

```bash
sudo apt install git -y
```

#### 4. Create Virtual Environment (Recommended)

```bash
python3 -m venv kslearn-env
source kslearn-env/bin/activate
```

#### 5. Install kslearn

**Option A: Git Clone**

```bash
git clone https://github.com/kashsightplatform/kslearn.git
cd kslearn
pip install -e .
```

**Option B: ZIP Download**

1. Download from GitHub:
   - Go to https://github.com/kashsightplatform/kslearn
   - Click "Code" → "Download ZIP"
   - Extract the ZIP file

2. Install:
   ```bash
   cd kslearn-main
   pip install -e .
   ```

#### 6. Create Alias (Optional)

Add to your `~/.bashrc` or `~/.zshrc`:

```bash
echo 'alias ksl="kslearn"' >> ~/.bashrc
source ~/.bashrc
```

#### 7. Verify and Launch

```bash
kslearn --version
kslearn
```

### Linux Distribution Specific

**Fedora/RHEL:**
```bash
sudo dnf install python3 python3-pip git -y
git clone https://github.com/kashsightplatform/kslearn.git
cd kslearn
pip3 install -e .
```

**Arch Linux:**
```bash
sudo pacman -S python python-pip git
git clone https://github.com/kashsightplatform/kslearn.git
cd kslearn
pip install -e .
```

**openSUSE:**
```bash
sudo zypper install python3 python3-pip git
git clone https://github.com/kashsightplatform/kslearn.git
cd kslearn
pip3 install -e .
```

---

## 🍎 macOS

### Prerequisites

- macOS 10.15 (Catalina) or later
- Terminal app

### Step-by-Step Installation

#### 1. Install Homebrew (if not installed)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

#### 2. Install Python

```bash
brew install python
```

#### 3. Install Git

```bash
brew install git
```

#### 4. Install kslearn

**Option A: Git Clone**

```bash
git clone https://github.com/kashsightplatform/kslearn.git
cd kslearn
pip3 install -e .
```

**Option B: ZIP Download**

1. Download from GitHub:
   - Visit https://github.com/kashsightplatform/kslearn
   - Click "Code" → "Download ZIP"
   - Double-click to extract

2. Install via Terminal:
   ```bash
   cd ~/Downloads/kslearn-main
   pip3 install -e .
   ```

#### 5. Verify and Launch

```bash
kslearn --version
kslearn
```

### macOS Troubleshooting

**Problem:** Permission denied
```bash
pip3 install --user -e .
```

**Problem:** Command not found
```bash
export PATH="$HOME/.local/bin:$PATH"
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
```

---

## 🪟 Windows

### Prerequisites

- Windows 10/11
- Administrator access

### Method 1: Standard Installation

#### 1. Install Python

1. Download Python from https://python.org
2. Run installer
3. ✅ **CHECK** "Add Python to PATH"
4. Click "Install Now"

#### 2. Install Git

1. Download from https://git-scm.com/download/win
2. Run installer with default options

#### 3. Open Command Prompt or PowerShell

Press `Win + R`, type `cmd`, press Enter

#### 4. Install kslearn

**Option A: Git Clone**

```cmd
git clone https://github.com/kashsightplatform/kslearn.git
cd kslearn
pip install -e .
```

**Option B: ZIP Download**

1. Download ZIP from GitHub
2. Extract to a folder (e.g., `C:\Users\YourName\Downloads\kslearn`)
3. Open Command Prompt in that folder:
   - Hold Shift + Right-click → "Open PowerShell window here"
4. Install:
   ```cmd
   pip install -e .
   ```

#### 5. Verify and Launch

```cmd
kslearn --version
kslearn
```

### Method 2: Windows Subsystem for Linux (WSL)

For better compatibility:

#### 1. Install WSL

```powershell
wsl --install
```

Restart computer when prompted.

#### 2. Open Ubuntu (WSL)

Search "Ubuntu" in Start Menu

#### 3. Follow Linux Instructions

```bash
sudo apt update
sudo apt install python3 python3-pip git -y
git clone https://github.com/kashsightplatform/kslearn.git
cd kslearn
pip3 install -e .
kslearn
```

### Windows Troubleshooting

**Problem:** `pip` not recognized
```cmd
python -m pip install -e .
```

**Problem:** Permission denied
```cmd
pip install --user -e .
```

**Problem:** Long path errors
```cmd
# Enable long paths in Registry
reg add HKLM\SYSTEM\CurrentControlSet\Control\FileSystem /v LongPathsEnabled /t REG_DWORD /d 1 /f
```

---

## 📥 Installation Methods

### Method 1: Git Clone (Recommended)

**Pros:**
- ✅ Easy to update (`git pull`)
- ✅ Get latest features
- ✅ Can contribute to project
- ✅ Smaller download size

**Cons:**
- ❌ Requires Git installed

**Commands:**
```bash
git clone https://github.com/kashsightplatform/kslearn.git
cd kslearn
pip install -e .
```

### Method 2: ZIP Download

**Pros:**
- ✅ No Git needed
- ✅ Works on any device with browser
- ✅ Simple for beginners

**Cons:**
- ❌ Larger download
- ❌ Manual updates (re-download)
- ❌ No version control

**Steps:**
1. Go to https://github.com/kashsight/kslearn
2. Click "Code" button
3. Click "Download ZIP"
4. Extract ZIP file
5. Open terminal in extracted folder
6. Run: `pip install -e .`

### Method 3: pip Install (Future)

When published to PyPI:

```bash
pip install kslearn
```

*Note: Not yet available on PyPI*

---

## ✅ Verification

### Check Installation

```bash
# Check version
kslearn --version

# Should output: kslearn v1.0.0
```

### Test All Features

```bash
# 1. Launch interactive mode
kslearn

# 2. Test Study Notes
kslearn study

# 3. Test Quiz
kslearn quiz --random

# 4. Test Knowledge Brain
kslearn brain

# 5. Test AI Chat (if tgpt installed)
kslearn chat
```

### Expected Output

```
╔══════════════════════════════════════════╗
║     ███╗   ██╗███████╗██╗    ██╗███████╗ ║
║     ████╗  ██║██╔════╝██║    ██║██╔════╝ ║
║     ██╔██╗ ██║█████╗  ██║ █╗ ██║███████╗ ║
║     ██║╚██╗██║██╔══╝  ██║███╗██║╚════██║ ║
║     ██║ ╚████║███████╗╚███╔███╔╝███████║ ║
║     ╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝ ╚══════╝ ║
╚══════════════════════════════════════════╝

📚 Welcome to kslearn - Your Learning Platform
```

---

## 🔧 Troubleshooting

### Common Installation Issues

#### "pip: command not found"

**Linux/macOS:**
```bash
python3 -m pip install -e .
```

**Windows:**
```cmd
python -m pip install -e .
```

**Termux:**
```bash
pkg install python-pip -y
```

#### "Permission denied"

**Solution 1: User install**
```bash
pip install --user -e .
```

**Solution 2: Virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install -e .
```

#### "No module named 'rich'"

Missing dependencies. Reinstall:
```bash
pip install -r requirements.txt
pip install -e . --force-reinstall
```

#### "kslearn: command not found" after install

**Linux/macOS:**
```bash
export PATH="$HOME/.local/bin:$PATH"
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

**Windows:**
Add to PATH manually:
1. Search "Environment Variables"
2. Edit PATH
3. Add: `C:\Users\YourName\AppData\Roaming\Python\Python3X\Scripts`

#### Installation hangs or fails

```bash
# Upgrade pip first
pip install --upgrade pip

# Clear cache
pip cache purge

# Install without cache
pip install -e . --no-cache-dir
```

### Platform-Specific Issues

#### Termux: "Wheel building failed"

```bash
pkg install build-essential -y
pkg install libffi -y
pip install -e .
```

#### macOS: "Xcode required"

```bash
xcode-select --install
```

#### Windows: "Visual C++ required"

Download: https://visualstudio.microsoft.com/visual-cpp-build-tools/

---

## 🗑️ Uninstallation

### Remove kslearn

```bash
# Uninstall package
pip uninstall kslearn

# Remove cloned directory
rm -rf kslearn  # Linux/macOS
rmdir /s kslearn  # Windows

# Remove config files
rm -rf ~/.kslearn
rm ~/.kslearnrc
```

### Remove Virtual Environment (if created)

```bash
rm -rf kslearn-env  # Linux/macOS
rmdir /s kslearn-env  # Windows
```

### Remove from PATH (if added)

**Linux/macOS:**
Edit `~/.bashrc` or `~/.zshrc` and remove:
```bash
alias ksl="kslearn"
```

**Windows:**
1. Search "Environment Variables"
2. Edit PATH
3. Remove kslearn entries

---

## 📊 Installation Comparison

| Platform | Difficulty | Time | Commands |
|----------|-----------|------|----------|
| **Termux** | Easy | 2 min | 5 |
| **Ubuntu** | Easy | 3 min | 6 |
| **macOS** | Easy | 3 min | 6 |
| **Windows** | Medium | 5 min | 6 |
| **WSL** | Medium | 5 min | 7 |

---

## 🎯 Post-Installation

### First Steps

1. **Launch kslearn:**
   ```bash
   kslearn
   ```

2. **Take the tour:**
   - Press `H` for Help
   - Explore Study Notes (Option 1)
   - Try a Quiz (Option 2)

3. **Configure settings:**
   ```bash
   kslearn config --edit
   ```

4. **Start learning!**
   - Begin with Study Notes
   - Take quizzes to test knowledge
   - Track progress (Option 4)

### Optional Enhancements

**Install AI Chat (tgpt):**
```bash
# Termux
pkg install termux-ai -y

# Other platforms - see tgpt documentation
```

**Create Desktop Shortcut:**

**Linux:**
```bash
echo '[Desktop Entry]
Name=kslearn
Exec=kslearn
Type=Application
Terminal=true
Categories=Education;' > ~/.local/share/applications/kslearn.desktop
```

**Windows:**
Create shortcut on desktop pointing to:
```
C:\path\to\python.exe -m kslearn
```

---

## 📞 Getting Help

### Resources

- **Documentation:** See `ADDING_CONTENT.md` for adding content
- **GitHub Issues:** https://github.com/kashsightplatform/kslearn/issues
- **Discussions:** https://github.com/kashsightplatform/kslearn/discussions

### Support

- **Report a Bug:** `kslearn --help` → GitHub Issues
- **Request Feature:** GitHub Issues → Feature Request
- **Ask Question:** GitHub Discussions

---

## 🎉 Success!

If you see the kslearn banner, you're ready to learn! 📚✨

```bash
kslearn
```

**Happy Learning!** 🚀

---

*Made with ❤️ for learners everywhere*
*kslearn v1.0.0 - JSON-Powered Educational Learning System*
