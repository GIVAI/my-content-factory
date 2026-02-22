# Nano Banana Thumbnails Module

YouTube thumbnail-specific prompts for Nano Banana (Gemini 2.5 Flash Image).

---

## When to Load

- "thumbnail", "превью", "обложка"
- "youtube cover", "miniature"
- Face swap for thumbnails
- Channel-specific thumbnails (DMG/DSG/DMES)

---

## Core Formula

```
┌───────────────────────────────────────────────────────────┐
│                                                           │
│  ┌──────────────────┐                                    │
│  │  TRIGGER TEXT    │                      ┌──────────┐  │
│  │  (color box)     │                      │  EXPERT  │  │
│  └──────────────────┘                      │  (right) │  │
│                                            │          │  │
│  ┌──────────┐                              │ EMOTION  │  │
│  │ IMPULSE  │◄─── arrow                    │          │  │
│  │ OBJECT   │                              └──────────┘  │
│  └──────────┘                                            │
│                                                           │
└───────────────────────────────────────────────────────────┘
```

### Elements

| Element | Position | Purpose |
|---------|----------|---------|
| Expert/Doctor | Right 1/3 | Authority, trust |
| Trigger Text | Top or center-left | Hook, curiosity |
| Impulse Object | Left 1/3 | Visual anchor |
| Arrow/Pointer | Between elements | Direction, connection |
| Background | Full frame | Context, mood |

### Rules

- **Max 3 objects** (expert + text + impulse object)
- **Max 3 colors** (brand + accent + neutral)
- **Text: 2-5 words** on colored box
- **Readable at 14% scale** (mobile sidebar)
- **Aspect ratio: 16:9** (1920x1080 or 1280x720)

---

## Template A: Expert + Impulse Object (TEXT)

```
A professional YouTube thumbnail image in 16:9 aspect ratio (1920x1080 pixels).

RIGHT SIDE (40%): A [age] [ethnicity] male doctor with [hair description] wearing [clothing], displaying [emotion expression] with [pose detail]. Face clearly visible, taking up significant portion of the right third.

LEFT SIDE (40%): [Impulse object description] with [visual treatment: golden circle border / red arrow pointing / red X overlay / green checkmark / subtle glow]. Object is prominent and immediately recognizable.

TEXT: Large bold text reading "[TRIGGER TEXT]" (maximum 5 words) on a [dark red #8B0000 / bright orange #FF6600] rectangular box with slight drop shadow, positioned [top-left / center-top]. White text, bold sans-serif font (Impact style), readable at small sizes.

BACKGROUND: [Dark blue gradient with subtle molecular formulas / Bright gradient yellow-to-orange / Blurred medical office]. Clean, not competing with foreground elements.

STYLE: High contrast, vibrant colors, professional medical channel aesthetic. Sharp focus on face and objects. Optimized for small display sizes.
```

---

## Template B: Face Swap (with reference)

```
Replace the person in [Image1] with the person from [Image2].

IDENTITY PRESERVATION (CRITICAL):
- Preserve EXACT facial features from [Image2]: bone structure, nose shape, eye spacing, jawline
- Preserve EXACT skin tone, texture, pores, any blemishes
- Preserve EXACT hairstyle, hair color, hairline
- NO beautification, NO smoothing, NO idealization
- NO age change, NO ethnicity drift
- Person MUST be 100% recognizable as the same individual from [Image2]

SCENE PRESERVATION:
- Keep ALL text overlays, graphic elements, and background from [Image1] unchanged
- Keep the exact composition and layout from [Image1]
- Match lighting direction and color temperature naturally

OUTPUT: Professional YouTube thumbnail, 16:9 aspect ratio. The result should look like the real person ([Image2]) was photographed in the thumbnail scene ([Image1]).
```

---

## Template C: Complex Scene (JSON)

```json
{
  "image_type": "YouTube thumbnail",
  "aspect_ratio": "16:9 (1920x1080)",
  "composition": {
    "left_third": {
      "element": "[impulse object description]",
      "treatment": "[circle with golden border / red arrow / X overlay / glow]",
      "size": "prominent, 30-40% of left area"
    },
    "center": {
      "text_overlay": {
        "content": "[TRIGGER TEXT - max 5 words]",
        "font": "bold sans-serif (Impact style)",
        "color": "white",
        "background_box": {
          "color": "[#8B0000 dark red / #FF6600 orange]",
          "style": "rectangular with slight shadow"
        },
        "position": "[top-left / center-top]"
      }
    },
    "right_third": {
      "subject": {
        "description": "[age] [ethnicity] male doctor/expert",
        "clothing": "[white lab coat / navy scrubs / casual polo]",
        "expression": "[shocked / thinking / concerned / confident]",
        "pose": "[hand on chin / hand raised / pointing / arms crossed]"
      }
    }
  },
  "background": {
    "type": "[gradient / blurred / solid]",
    "colors": "[specific hex codes]",
    "elements": "[molecular formulas / medical shelves / kitchen / none]"
  },
  "style": {
    "aesthetic": "professional medical YouTube channel",
    "quality": "high contrast, vibrant colors, sharp text",
    "optimization": "readable at small sizes, mobile-friendly"
  },
  "identity_preservation": {
    "reference": "[Image2]",
    "instruction": "Preserve exact facial features from reference. Must look 100% identical. No beautification."
  }
}
```

---

## Identity Lock for Medical Thumbnails

When using doctor reference [Image], add this block:

```
IDENTITY LOCK for doctor from [Image]:
- Preserve EXACT facial features: bone structure, nose shape, eye spacing, jawline
- Preserve EXACT skin tone, texture, pores, and any imperfections
- Preserve EXACT hairstyle, hair color, and hairline
- NO beautification, NO smoothing, NO idealization
- NO age change, NO ethnicity drift, NO face morphing
- Doctor MUST be 100% recognizable as the same individual
- If identity cannot be preserved perfectly, DO NOT generate

MEDICAL PROFESSIONAL APPEARANCE:
- White lab coat OR navy medical scrubs
- Stethoscope around neck (optional)
- Clean, professional, trustworthy appearance
- Direct or 3/4 face angle toward camera
```

---

## Emotion Library

| Emotion | Prompt Description | Use When |
|---------|-------------------|----------|
| **Shocked** | "eyes wide open, eyebrows raised high, mouth slightly open in surprise" | Revealing secrets, myth-busting |
| **Thinking** | "hand on chin, slight head tilt, contemplative expression, one eyebrow raised" | Analysis, comparisons |
| **Concerned** | "furrowed brow, slight frown, serious expression, worried eyes" | Warning content, problems |
| **Confident** | "direct eye contact, slight knowing smile, shoulders back" | Solutions, protocols |
| **Happy** | "genuine smile showing teeth, warm expression, relaxed posture" | Positive results, success |
| **Skeptical** | "one eyebrow raised, slight smirk, head tilted, questioning look" | Debunking, truth reveals |
| **Urgent** | "intense gaze, leaning forward, finger pointing, emphatic expression" | Must-know information |

---

## Object Arrangements

### Visual Treatments

| Treatment | Prompt Description | Use For |
|-----------|-------------------|---------|
| **Golden Circle** | "surrounded by a golden circular border with subtle glow" | Highlighting good items |
| **Red Arrow** | "large red arrow pointing at the object from above-left" | Drawing attention |
| **Red X** | "large red X overlay on the object" | Warning, avoid |
| **Green Checkmark** | "green checkmark next to the object" | Approved, recommended |
| **Subtle Glow** | "soft glowing aura around the object" | Emphasis |
| **Circular Frame** | "object placed inside a white circular frame with shadow" | Clean presentation |

### Multi-Object Arrangement

```
For 2-3 impulse objects, arrange in:
- Horizontal row (objects side by side)
- Diagonal cascade (top-left to bottom-right)
- Overlapping circles (each object in its own circle)

Example: "Three food items (tomato, beet, pumpkin seeds) arranged in overlapping circles, left-to-right, each in a white circular frame with golden border"
```

---

## Channel-Specific Styles

### Medical Expert (Professional)

```json
{
  "doctor": {
    "clothing": "white lab coat over light blue shirt with dark tie",
    "alternative": "navy blue medical scrubs",
    "accessories": "stethoscope around neck"
  },
  "emotions": ["thinking (hand on chin)", "shocked (eyes wide)", "concerned (raised eyebrow)"],
  "text_style": {
    "box_color": "#8B0000 dark red or #FF0000 bright red",
    "text_color": "white, bold sans-serif"
  },
  "background": "dark blue gradient with subtle molecular formulas",
  "color_palette": ["red", "white", "dark blue"],
  "impulse_objects": ["supplements/pills", "foods", "anatomy diagrams", "medical equipment"]
}
```

### Lifestyle/Wellness Expert

```json
{
  "expert": {
    "clothing": "casual polo or smart casual attire",
    "style": "approachable, friendly, relatable"
  },
  "emotions": ["big smile (positive)", "thumbs up", "playful"],
  "text_style": {
    "box_color": "#FF6600 orange or #4CAF50 green",
    "text_color": "white, bold"
  },
  "background": "bright gradient (yellow-orange or green-yellow)",
  "color_palette": ["orange", "yellow", "green", "white"],
  "special": {
    "metaphors": "use visual metaphors relevant to your niche",
    "style": "playful illustrations, relatable imagery"
  }
}
```

---

## Color Contrast Rules

**High CTR color combinations:**

| Niche | Primary | Accent | Background |
|-------|---------|--------|------------|
| Medical/Health | Red | White | Dark blue |
| Nutrition/Diet | Green | Orange | Light gradient |
| Energy/Performance | Red | Yellow | Black |
| Sleep/Recovery | Blue | White | Dark gradient |
| Scientific | Purple | White | Dark blue |

**Contrast > Beauty:** High contrast ugly colors outperform pretty low-contrast colors by +30% CTR.

---

## Output Checklist

Before generating thumbnail prompt:

- [ ] Aspect ratio: 16:9 (1920x1080 or 1280x720)
- [ ] Doctor/expert position: right side (40%)
- [ ] Emotion clearly described
- [ ] Impulse object with visual treatment
- [ ] Text content (2-5 words) and box color
- [ ] Background described (clean, not competing)
- [ ] Max 3 colors
- [ ] Identity Lock included (if using reference)
- [ ] "Readable at small sizes" mentioned
- [ ] Clean output (no commentary, immediately usable)

---

## Quick Commands

| Command | Template |
|---------|----------|
| "thumbnail: [topic]" | Template A (TEXT) |
| "face swap thumbnail" | Template B |
| "complex thumbnail" | Template C (JSON) |
| "medical thumbnail" | Template A + Medical Expert style |
| "lifestyle thumbnail" | Template A + Lifestyle Expert style |

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Face looks different | Add full Identity Lock block |
| Text not readable | Increase font size mention, add "bold" |
| Too busy composition | Reduce to 3 objects max |
| Colors clashing | Stick to channel palette |
| Object not prominent | Add visual treatment (circle, glow) |
| Wrong aspect ratio | Explicitly state "16:9 1920x1080" |

---

*Part of nano-banana skill. Load with: "thumbnail", "превью", "обложка"*
