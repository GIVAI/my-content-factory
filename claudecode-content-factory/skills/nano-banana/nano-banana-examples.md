# Nano Banana Examples

Примеры трансформации простых идей в профессиональные промпты.

---

## Reference Image Operations

### Face Swap (MrBeast Style Thumbnail)

**Input**: "Хочу обложку как у MrBeast с моим фото"

**Output**:
```
Replace the man from [Image1] with the person from [Image2]. Very important to preserve facial features, body type, and clothing of the person so they look like themselves. They should organically and realistically fit into the atmosphere of [Image1].
```

---

### Selfie with Celebrity

**Input**: "Хочу реалистичное селфи с Илоном Маском"

**Output**:
```
Replace the girl in the selfie from [Image1] with Elon Musk with the girl from [Image2]. Keep the new girl exactly recognizable — same facial features, proportions, skin texture, and natural look. No beauty filters, no smoothing, no plastic skin, no blur, no makeup changes. She should smile softly with her mouth closed. Match the lighting and angle of the original photo - the result must look like a real iPhone selfie taken by the girl herself. Keep her outfit exactly the same as the girl in [Image2] photo. Keep the background, Elon Musk, the framing and the 16:9 aspect ratio unchanged. Do NOT change the pose, do NOT redesign the scene, only perform a realistic face-swap with minimal editing. Make the output look natural, unedited and as close to an authentic real-life selfie as possible.
```

---

### Photo Upscaling

**Input**: "Улучши качество этого фото"

**Output**:
```
Enhance and upscale [Image1], preserving composition and colors without changes. Remove blur and make skin realistic and detailed: clear pores, light wrinkles, and natural transitions between shadow and light. Preserve lighting tone and background, improve edge sharpness around eyes, eyelashes, lips, and hair strands, so the portrait looks like high-class beauty photography with natural, non-plastic skin.
```

---

### Clothing Change

**Input**: "Замени леггинсы на широкие штаны"

**Output**:
```
Keep the person from [Image1] unchanged, but replace her athletic leggings with the clothing from [Image2]. Preserve pose, body proportions, and facial features. Apply the color, texture, and style of the pants from [Image2]. High-quality, realistic, accurate detailing.
```

---

### Multi-Object Composition

**Input**: "Объедини туфли, шарики и платье с девочкой в одно фото"

**Output**:
```
Combine multiple images ([Image1], [Image2], [Image3], [Image4]) into one cohesive image. Preserve the recognizability of all key objects while maintaining their proportions and details. Blend images naturally using unified lighting, shadows, perspective, and style. Photorealistic, high resolution, seamless integration.
```

---

### Camera Angle Change

**Input**: "Покажи эту сцену сверху"

**Output**:
```
Recreate the scene from [Image1] from a different angle. Preserve the identity, body proportions, and clothing of the subjects. Use the same background as [Image1], with photorealistic lighting, natural shadows, and high-quality details. Create scene: Bird's eye view (from above).
```

---

## Text-to-Image Examples

### Simple Input → Full Prompt

**Input**: "guy in car"

**Clarifying Questions**:
- What type of car? (vintage, modern, sports car)
- Setting? (city, highway, scenic location)
- Mood? (dramatic, casual, adventurous)
- Style? (photorealistic, cinematic)

**User**: Vintage car, coastal highway, adventurous, cinematic

**Output**:
```
A confident man in his mid-30s with short dark hair and stubble, wearing a brown leather jacket and aviator sunglasses, sitting relaxed in the driver's seat of a vintage red 1967 Ford Mustang convertible with the top down. His left hand rests casually on the steering wheel while his right arm is draped over the door. The car is parked on a scenic coastal highway overlooking the Pacific Ocean at golden hour, with dramatic cliffs and crashing waves visible in the background. The scene is illuminated by dramatic golden hour lighting streaming through the driver's side window, creating warm highlights on his face and cool shadows on the passenger side, with a subtle lens flare from the setting sun. Shot in a cinematic style reminiscent of 1990s car commercials, with vibrant saturated colors and a nostalgic atmosphere. Captured on Sony A7R IV with 50mm f/1.8 lens, shallow depth of field creating bokeh effect on the ocean background, medium close-up shot from a slightly low angle emphasizing the subject's confidence and sense of freedom. Ultra-sharp, highly detailed with intricate textures visible in the leather jacket and car interior, 8K resolution, professional commercial photography quality. Adventurous and carefree mood with a sense of escapism, warm nostalgic atmosphere reminiscent of road trip films.
```

---

### Portrait Request

**Input**: "portrait of a woman"

**User**: Late 30s, CEO, modern office, corporate editorial

**Output**:
```
A professional portrait photograph of a confident female CEO in her late 30s, with shoulder-length auburn hair styled in a sleek professional cut, wearing a tailored navy blue business suit with a crisp white blouse. She stands with an upright, commanding posture, slight smile conveying approachable authority, arms relaxed at her sides. The setting is a modern glass-walled corner office with floor-to-ceiling windows, revealing a Manhattan skyline at sunset in the soft-focus background. The scene is illuminated by soft, diffused window light from the side, creating gentle shadows that add dimension without harshness, complemented by subtle fill light to ensure even facial lighting. Shot in a clean, professional editorial style typical of business magazines like Fortune or Forbes. Captured on Canon EOS R5 with 85mm f/1.8 portrait lens, shallow depth of field isolating the subject while maintaining recognizable office environment, shot from eye level with subject slightly off-center following rule of thirds composition. Tack sharp focus on eyes and face, highly detailed with visible fabric texture in the suit, 8K resolution, magazine-quality professional photography.
```

---

### Creative/Fantasy Scene

**Input**: "wizard in forest"

**User**: Old sage, enchanted mystical forest, twilight, fantasy digital painting

**Output**:
```
A wise elderly wizard with a long flowing white beard and silver hair, wearing deep purple and midnight blue robes embroidered with golden celestial patterns, holding an ancient gnarled wooden staff topped with a glowing crystal orb. He stands in a mystical enchanted forest during the blue hour twilight, surrounded by massive ancient oak trees with twisted roots and luminescent mushrooms glowing softly at their base. Ethereal wisps of magic float through the air around him, and fireflies create points of warm light throughout the scene. The forest floor is covered in soft moss and magical glowing flowers in shades of blue and purple. The scene is illuminated by a combination of the magical glow from the staff and mushrooms (creating pools of cyan and violet light), the last rays of twilight filtering through the canopy (soft purple-blue ambient light), and scattered firefly lights adding warm golden points. Created in a high-quality fantasy digital painting style with rich colors and atmospheric depth, similar to concept art from fantasy games. The composition places the wizard slightly off-center with ancient trees framing the scene, creating depth with layers of foreground mushrooms, the wizard in midground, and misty forest depths in background. Highly detailed with intricate patterns on robes, visible texture in bark and moss, magical particle effects, and atmospheric volumetric lighting creating god rays through the trees.
```

---

### Product Photography

**Input**: "smartphone on table"

**User**: Minimal marble surface, clean background, dramatic but professional, commercial ad

**Output**:
```
A sleek modern smartphone with an edge-to-edge display showing a vibrant abstract wallpaper, positioned at a slight angle on a pristine white marble surface with subtle gray veining. The phone casts a soft shadow on the surface. The background is a gradient from light gray to white, completely clean and minimal to focus attention on the product. The scene is illuminated by professional studio lighting with a main key light at 45 degrees creating subtle highlights along the phone's metallic edges, complemented by a large softbox overhead for even diffused light, and a subtle rim light from behind to separate the phone from the background. Shot in a high-end commercial product photography style typical of Apple or Samsung advertisements, with exceptional attention to reflections and material quality. Captured on Phase One XF with 80mm macro lens, f/8 for sharp focus throughout the product while maintaining clean background, shot from a slightly elevated angle to show both the screen and the slim profile. Ultra-sharp, crystal clear with every detail visible including screen pixels, metallic finish, and marble texture, 8K resolution, award-winning commercial product photography quality.
```

---

## JSON Format Examples

### Times Square Night Scene

```json
{
  "scene": {
    "location": "Times Square, New York",
    "time": "Rainy night",
    "composition": {
      "left_side": [
        {"type": "LED billboard", "style": "vertical"},
        {"type": "curved LED screen", "detail": "above Hershey's store"}
      ],
      "right_side": {
        "subject_position": "near curb",
        "traffic": {"vehicles": "city taxis", "details": "brake lights"}
      }
    },
    "environment": {
      "ground": "wet asphalt",
      "reflection_colors": ["neon magenta", "icy blue"],
      "atmosphere": ["electric", "intimate"]
    }
  },
  "subject": {
    "identity": "Uploaded subject",
    "face_requirement": "Do not change facial features. Must look 1000% identical.",
    "pose": "Relaxed, facing camera",
    "outfit": {
      "jacket": {
        "material": "black faux-leather varsity",
        "design": {
          "cobalt_panel": true,
          "embroidery": "Vintage script",
          "patch": "1987 stitched on sleeve"
        }
      }
    }
  },
  "style": {
    "resolution": "HD",
    "aesthetic": ["realistic", "natural", "authentic"],
    "camera": "iPhone"
  }
}
```

---

### Viking Survivor Portrait

```json
{
  "subject": {
    "description": "A lone Viking survivor trekking through a burned village",
    "age": "late 30s",
    "expression": "fierce, exhausted, determined",
    "hair": {
      "color": "dirty blonde",
      "style": "long, tangled, partially braided with frost"
    },
    "clothing": {
      "top": {
        "type": "fur-lined leather tunic",
        "details": "cut marks, smoky residue, torn seams"
      },
      "bottom": {
        "type": "wool trousers",
        "details": "mud splatter, frayed edges"
      }
    },
    "face": {
      "preserve_original": true,
      "makeup": "war paint smudged, dried blood, windburn"
    }
  },
  "accessories": {
    "jewelry": {
      "necklace": "hand-carved rune pendant",
      "wrist": "leather bracer with axe scrapes"
    },
    "prop": {
      "type": "battle-worn Viking axe",
      "details": "blood stains, chipped blade"
    }
  },
  "photography": {
    "camera_style": "Dark cinematic realism with subtle grain",
    "angle": "mid-wide shot, slightly low angle",
    "aspect_ratio": "16:9"
  },
  "background": {
    "setting": "ruined Viking settlement near a fjord",
    "elements": [
      "collapsed longhouse",
      "smoldering fire pit",
      "snow-covered mountains in distance",
      "ravens circling overhead"
    ],
    "atmosphere": "somber, cold, mythic survival energy",
    "lighting": "misty morning light, diffused and cold"
  }
}
```

---

## Pattern: The 7-Category Framework

Every prompt follows this structure:

1. **Subject Specification** (who/what + details)
2. **Environment** (where + spatial layers)
3. **Lighting** (type + direction + quality)
4. **Style** (artistic/photographic approach)
5. **Camera/Technical** (equipment + settings)
6. **Composition** (framing + perspective)
7. **Quality/Mood** (atmosphere + technical specs)

Expand each category systematically while maintaining natural, descriptive language.
