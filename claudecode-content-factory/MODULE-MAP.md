# Module Map — Content Factory

> Which files belong to which module

---

## Installation Types

| Type | Description | Use Case |
|------|-------------|----------|
| **Full** | All modules included | Maximum flexibility |
| **Modular** | Choose only needed modules | Save disk space, focus |
| **Core Only** | Basic system without content modules | Custom setup |

---

## CORE (Always Installed)

### System Files
```
CLAUDE.md                    # Main router
README.md                    # Quick start
VERSION                      # Version tracking
CHANGELOG.md                 # Update history
UPDATE-GUIDE.md              # Upgrade instructions
```

### Core Agents
```
agents/strategy/
├── project-architect.md     # Project creation
├── selling-meanings.md      # Selling meanings agent
└── ...

agents/analytics/
├── analyst.md               # Metrics analysis
└── critics/                 # Three critics
    ├── sales-critic.md
    ├── creative-critic.md
    └── structure-critic.md
```

### Universal Skills
```
skills/
├── selling-meanings/        # Psychology, positioning
├── prompt-engineer/         # Prompt creation
├── storytelling/            # Storytelling techniques
├── launch/                  # Product Launch Formula
├── skill-creator/           # Create new skills
└── learning-processor/      # Process learning materials
```

### Project Template
```
projects/_template/          # Modular multi-direction template
```

### Documentation
```
docs/
├── USER-GUIDE.md            # Complete guide
├── inheritance-architecture.md  # How system works
├── troubleshooting.md       # Common issues
└── ...
```

---

## MODULE 1: YouTube (Long-form)

**For:** Long-form videos (10-20+ minutes)

### Files Included
```
skills/youtube/      # YouTube methodology
├── SKILL.md                 # Main skill file
├── youtube-hooks.md         # Hook patterns
├── youtube-structure.md     # Video structure
├── youtube-retention.md     # Retention tactics
├── youtube-seo.md           # SEO optimization
└── ...

agents/production/
└── youtube.md               # YouTube producer agent

docs/
└── youtube-guide.md         # YouTube setup guide (if exists)
```

**Commands Enabled:**
- `youtube script [topic]`
- `youtube hook [topic]`
- `youtube package [script]`
- `youtube review [script]`

**Dependencies:** None

---

## MODULE 2: YouTube Shorts

**For:** Vertical videos (30-60 seconds)

### Files Included
```
skills/youtube/      # Uses YouTube skill (hooks section)

agents/production/
└── vertical-content.md      # Vertical content agent

docs/
└── shorts-guide.md          # Shorts setup guide (if exists)
```

**Commands Enabled:**
- `shorts [topic]`
- `shorts series [topic]`
- `shorts hook [topic]`

**Dependencies:** Shares youtube skill with MODULE 1

---

## MODULE 3: Threads

**For:** Text posts for Threads platform

### Files Included
```
skills/threads/      # Threads methodology
├── SKILL.md                 # Main skill file
├── threads-visp.md          # VISP technique
├── threads-hooks.md         # Hook formulas
└── ...

agents/production/
└── threads.md               # Threads writer agent

docs/
└── threads-guide.md         # Threads setup guide (if exists)
```

**Commands Enabled:**
- `threads post [topic]`
- `threads series [topic]`
- `threads analyze [screenshot]`
- `threads review`

**Dependencies:** None

---

## MODULE 4: Instagram Reels

**For:** Instagram Reels (vertical video content)

### Files Included
```
skills/reels/        # Reels methodology
├── SKILL.md                 # Main skill file
├── reels-visp.md            # VISP formula
├── reels-hooks.md           # Hook patterns
└── ...

agents/production/
└── vertical-content.md      # Vertical content agent

docs/
└── reels-guide.md           # Reels setup guide (if exists)
```

**Commands Enabled:**
- `reels [topic]`
- `reels series [topic]`
- `reels hook [topic]`

**Dependencies:** None

---

## MODULE 5: Instagram Carousel

**For:** Multi-slide Instagram posts

### Files Included
```
skills/carousel/     # Carousel methodology
├── SKILL.md                 # Main skill file
├── carousel-design.md       # Design rules
├── carousel-structure.md    # Content structure
└── ...

agents/production/
└── threads.md               # Uses threads agent (adapted)

docs/
└── carousel-guide.md        # Carousel setup guide (if exists)
```

**Commands Enabled:**
- `carousel [topic]`
- `carousel outline [topic]`
- `carousel series [topic]`

**Dependencies:** Uses threads agent for text structure

---

## MODULE 6: Telegram

**For:** Telegram channel posts

### Files Included
```
skills/telegram/     # Telegram best practices (if exists)

agents/production/
└── threads.md               # Uses threads agent (adapted for longer form)

docs/
└── telegram-guide.md        # Telegram setup guide (if exists)
```

**Commands Enabled:**
- `telegram post [topic]`
- `telegram series [topic]`
- `telegram newsletter`

**Dependencies:** Uses threads agent structure

---

## MODULE 7: Nano Banana

**For:** Image prompt generation and YouTube thumbnails

### Files Included
```
skills/nano-banana/  # Nano Banana prompt engineering
├── SKILL.md                 # Main skill file
├── nano-banana-thumbnails.md  # Thumbnail prompts
├── nano-banana-identity.md  # Identity lock
└── ...

agents/production/
└── thumbnail-generator.md   # Thumbnail generator agent

docs/
└── nano-banana-guide.md     # Nano Banana guide (if exists)
```

**Commands Enabled:**
- `thumbnail for [topic]`
- `image prompt [description]`
- `face swap thumbnail`

**Dependencies:** None

---

## Dependency Chart

```
CORE (required)
│
├──> MODULE 1: YouTube ──────────┐
│                                │
├──> MODULE 2: YouTube Shorts ───┤ (shares skill)
│                                │
├──> MODULE 3: Threads ──────────┼──> MODULE 5: Carousel
│                                │   (uses agent)
│                                │
├──> MODULE 4: Instagram Reels   │
│                                │
├──> MODULE 6: Telegram ─────────┘
│    (uses threads agent)
│
└──> MODULE 7: Nano Banana
```

---

## Installation Examples

### Example 1: YouTube Creator
```bash
./install.sh ~/my-factory

Modules: 1, 2, 7
# YouTube Long + Shorts + Thumbnails
```

### Example 2: Text-Only Creator
```bash
./install.sh ~/my-factory

Modules: 3, 6
# Threads + Telegram
```

### Example 3: Instagram Focus
```bash
./install.sh ~/my-factory

Modules: 4, 5
# Reels + Carousel
```

### Example 4: All Platforms
```bash
./install.sh ~/my-factory

Modules: A
# All modules installed
```

### Example 5: Core Only (Custom Setup)
```bash
./install.sh ~/my-factory

Modules: S
# Core only, add modules manually later
```

---

## Manual Module Installation

If you want to add modules after initial installation:

### 1. Copy Skill
```bash
cp -r skills/{module}/ ~/my-factory/skills/
```

### 2. Copy Agent
```bash
cp agents/production/{agent}.md ~/my-factory/agents/production/
```

### 3. Copy Docs (optional)
```bash
cp docs/{module}-guide.md ~/my-factory/docs/
```

---

## Removing Modules

To remove an unused module:

### 1. Remove Skill
```bash
rm -rf ~/.../my-factory/skills/{module}/
```

### 2. Remove Agent
```bash
rm ~/.../my-factory/agents/production/{agent}.md
```

**Note:** Removing core files may break the system. Only remove content modules.

---

## Module Sizes

Approximate disk space per module:

| Module | Skill | Agent | Total |
|--------|-------|-------|-------|
| **Core** | 2-3 MB | 500 KB | ~3-4 MB |
| YouTube | 300 KB | 50 KB | ~350 KB |
| Shorts | (shared) | 30 KB | ~30 KB |
| Threads | 150 KB | 30 KB | ~180 KB |
| Reels | 150 KB | (shared) | ~150 KB |
| Carousel | 100 KB | (shared) | ~100 KB |
| Telegram | 50 KB | (shared) | ~50 KB |
| Nano Banana | 200 KB | 40 KB | ~240 KB |

**Full install:** ~5 MB
**Modular install (3 modules):** ~4 MB

---

## Version Compatibility

| Module | Min Core Version | Notes |
|--------|------------------|-------|
| All modules | v2.0+ | Requires inheritance architecture |

---

*Last updated: 2026-01-22*
