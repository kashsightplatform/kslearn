# 🔐 kslearn Content Selling Guide

## Your Business Model

```
Open Source App (MIT)  +  Sold Encrypted Content
```

Like: Free Kindle app, paid ebooks. The **code is free**, the **content costs money**.

- Your GitHub repo is public (MIT license)
- Anyone can clone and run the app
- But the **notes/quizzes JSON files are encrypted**
- Buyers get a unique **activation key** to unlock what they purchased

---

## How It Works

### For You (the seller)

```bash
# 1. You create/edit notes as plain JSON
nano data/notes/advanced_physics.json

# 2. Encrypt the content you want to sell
python encrypt_content.py encrypt --key "YOUR-MASTER-KEY"

# 3. Verify decryption works
python encrypt_content.py decrypt --key "YOUR-MASTER-KEY" --dry

# 4. Delete backups after confirming
find data/ -name '*.bak' -delete

# 5. The .enc files are what you distribute to buyers
# The .json files stay on YOUR machine only
```

### For Buyers (your users)

```bash
# 1. They clone and install your app (free, open source)
git clone https://github.com/kashsight/kslearn
cd kslearn
pip install .

# 2. They get the encrypted .enc files from you
#    (downloaded after purchase, or included in the repo)

# 3. They activate with the key you gave them
kslearn activate
# Enter: ABC123-DEF456-789 (the key you sold them)

# 4. Content unlocks automatically — they can study now
kslearn
```

---

## Step-by-Step: Preparing Content for Sale

### Step 0: Your Content Key

The default key is `kslearn2026` — stored obfuscated in `kslearn/loader.py`:

```python
_PARTS = [b'a3NlYXJu', b'MjAyNg==']  # base64 of "kslearn" + "2026"
```

**To change the key for future updates:**

```bash
# Generate new base64 parts for your new key
python3 -c "
import base64
key = 'your-new-key-here'
# Split key into 2 parts and base64-encode each
mid = len(key) // 2
p1 = base64.b64encode(key[:mid].encode()).decode()
p2 = base64.b64encode(key[mid:].encode()).decode()
print(f'_PARTS = [b\"{p1}\", b\"{p2}\"]')
print(f'Your key: {key}')
"
```

Then:
1. Update `_PARTS` in `kslearn/loader.py` with the new parts
2. Decrypt content with old key
3. Re-encrypt with new key

### Step 1: Create your content as normal JSON

```
data/notes/advanced_physics.json   ← your work
data/notes/python_mastery.json     ← your work
data/quizzes/physics_quiz.json     ← your work
```

### Step 2: Encrypt the premium content

```bash
# Dry run first (safe — previews only)
python encrypt_content.py encrypt --key "kslearn-premium-2026" --dry

# Encrypt for real
python encrypt_content.py encrypt --key "kslearn-premium-2026"
```

Result:
```
data/notes/advanced_physics.json.enc   ← encrypted (useless without key)
data/notes/python_mastery.json.enc     ← encrypted (useless without key)
data/notes/basic_math.json             ← free (still plain JSON)
```

### Step 3: Generate unique keys per buyer (optional but recommended)

Instead of one master key, generate unique keys per customer:

```python
# Generate a unique key for each buyer
import hashlib
import secrets

def generate_buyer_key(buyer_email):
    """Generate a unique activation key tied to a buyer."""
    random_salt = secrets.token_hex(8)
    raw = f"kslearn-{buyer_email}-{random_salt}-2026"
    return hashlib.sha256(raw.encode()).hexdigest()[:24].upper()

# Example:
key = generate_buyer_key("customer@email.com")
print(key)  # e.g., "A3F8B2C9D1E4F7A0B5C8D2E6"
```

**Important:** If you use unique keys per buyer, you need to encrypt the content separately for each key. The simpler approach is **one master key** for all buyers.

### Step 4: Distribute

| What | Where |
|---|---|
| App code (`.py` files) | GitHub (public, MIT license) |
| Free content (plain `.json`) | GitHub (public) |
| Premium content (`.enc` files) | GitHub or download after purchase |
| Activation key | Sent to buyer after payment (email, receipt page) |

### Step 5: Buyer activates

```bash
kslearn activate --key "A3F8B2C9D1E4F7A0B5C8D2E6"
```

The key is saved to `~/.kslearn/licenses/content.key` and used automatically every time the app runs.

---

## Encryption Levels

### Option A: One master key for all buyers (simplest)

```bash
# You encrypt content once with your master key
python encrypt_content.py encrypt --key "kslearn-master-key"

# Every buyer uses the same key
kslearn activate --key "kslearn-master-key"
```

**Pros:** Simple, one encryption step
**Cons:** If one buyer leaks the key, everyone can use it

### Option B: Unique key per buyer (more secure)

```bash
# For each buyer, encrypt with their unique key
python encrypt_content.py encrypt --key "BUYER-UNIQUE-KEY-ABC123"

# Only this buyer can decrypt
kslearn activate --key "BUYER-UNIQUE-KEY-ABC123"
```

**Pros:** If one buyer leaks, others aren't affected. You can revoke individuals.
**Cons:** You must encrypt separately for each buyer

### Option C: Tiered content

```
Free tier:    Plain JSON files (in the repo, anyone can read)
Premium tier: Encrypted .enc files (need activation key)
```

This is the recommended approach. Include some free content to attract users, sell the premium content.

---

## Commands Reference

### For you (seller)

| Command | Purpose |
|---|---|
| `python encrypt_content.py encrypt --key SECRET` | Encrypt premium content |
| `python encrypt_content.py decrypt --key SECRET` | Decrypt to edit content |
| `python encrypt_content.py status` | See which files are encrypted |
| `python encrypt_content.py encrypt --key SECRET --dry` | Preview before encrypting |
| `find data/ -name '*.bak' -delete` | Clean up backup files |

### For buyers (users)

| Command | Purpose |
|---|---|
| `kslearn activate` | Enter their purchased activation key |
| `kslearn activate --key ABC123` | Activate directly |
| `kslearn` | Run app — encrypted content auto-unlocks |

### What buyers see without a key

```
┌──────────────────────────────────────────┐
│ 🔒 Premium content detected!             │
│                                          │
│ You have encrypted content that needs     │
│ activation.                               │
│ Run kslearn activate to enter your        │
│ license key and unlock purchased notes.   │
└──────────────────────────────────────────┘
```

---

## How the Auto-Decrypt Works

When the app loads notes or quizzes:

```
1. Loader finds: data/notes/advanced_physics.json.enc
2. Reads user's key from: ~/.kslearn/licenses/content.key
3. Decrypts in memory (never writes decrypted to disk)
4. Returns the content to the app normally
5. User sees notes/quizzes like nothing is encrypted
```

The encrypted files **never get written to disk as plain JSON**. Decryption happens entirely in memory.

---

## Directory Structure (what buyers get)

```
kslearn/
├── kslearn/              ← Python app code (open source, MIT)
│   ├── cli.py
│   ├── loader.py         ← auto-decrypts .enc files
│   └── ...
├── data/
│   ├── notes/
│   │   ├── basic_math.json        ← FREE (plain JSON)
│   │   ├── advanced_physics.json.enc  ← PREMIUM (encrypted)
│   │   └── python_mastery.json.enc    ← PREMIUM (encrypted)
│   └── quizzes/
│       ├── general_quiz.json      ← FREE (plain JSON)
│       └── physics_quiz.json.enc  ← PREMIUM (encrypted)
├── encrypt_content.py      ← Your encryption tool
├── PROTECTION.md           ← This file
└── README.md
```

---

## Security Reality

| Who | What they can do |
|---|---|
| Random person cloning your repo | Can read the app code ✅ but NOT the encrypted content ❌ |
| Buyer who purchased | Can read content they paid for ✅ |
| Buyer who shares their key | Others can use that key (unless you use unique keys) |
| Skilled developer | Can eventually reverse-engineer if they really try |

**Bottom line:** This stops ~95% of unauthorized access. A determined attacker with Python skills can eventually extract the key, but most people just want to use the app, not crack it.

---

## Recommended Setup for Selling

1. **Keep one master encryption key** (store it securely, not in git)
2. **Encrypt premium content once** with that key
3. **Include .enc files in the repo** (they're useless without the key)
4. **Send the key only to paying customers** (via email, receipt page, etc.)
5. **Keep free content as plain JSON** to attract users
6. **Never commit the master key to git** (add it to `.gitignore`)

### Your workflow:

```
Create content → Encrypt with master key → Push .enc to GitHub
                                               ↓
                                    Buyer purchases → Gets key
                                               ↓
                                    Buyer runs: kslearn activate
                                               ↓
                                    Content unlocks ✅
```
