boat_in_valley = {
    "prompt": "A scene of a {{main_subject}} in a {{location}} at {{time_of_day}}, mist rolling between pine trees. Soft golden light touches snow-capped peaks. Foreground shows a reflective lake with a lone wooden boat. The scene feels {{mood}}, with subtle depth fog and atmospheric perspective.",
    "style": {
    "lighting": "golden hour sunlight with soft bloom",
    "color_palette": "warm oranges and cool blues",
    "composition": "rule of thirds, cinematic depth",
    "materials": "natural, slightly glossy water surface",
    "camera": "50mm lens equivalent, shallow depth of field"
    },
    "parameters": {
      "main_subject": "boat",
      "location": "vast mountain valley",
      "time_of_day": "sunrise",
      "weather": "misty",
      "mood": "serene and cinematic",
      "palette": ["#FFD580", "#6BA3FF", "#B4D6D3"]
    },
    "medium": "photorealistic 3D render or high-resolution digital painting",
    "size": "1920x1080"
}

tesla_card = {
    "prompt": "A futuristic trading card with a dark, moody neon aesthetic and soft sci-fi lighting. The card features a semi-transparent, rounded rectangle with slightly muted glowing edges, appearing as if made of holographic glass.  At the center is a large glowing logo of {{logo}}, with no additional text or label, illuminated with a smooth gradient of {{colors}}, but not overly bright. The reflections on the card surface should be subtle, with a slight glossy finish catching ambient light. The background is a dark carbon fiber texture or deep gradient with soft ambient glows bleeding into the edges. Add subtle light rays streaming down diagonally from the top, giving the scene a soft cinematic glow. Apply light motion blur to the edges and reflections to give the scene a sense of depth and energy, as if it's part of a high-end tech animation still. Below the card, include realistic floor reflections that mirror the neon edges and logo—slightly diffused for a grounded, futuristic look. Text elements are minimal and softly lit: top-left shows '{{ticker}}', top-right has a stylized signature, and the bottom displays '{{company_name}}' with a serial number '{{card_number}}', a revenue badge reading '{{revenue}}', and the year '{{year}}'. Typography should have a faint glow with slight blurring, and all elements should feel premium, elegant, and softly illuminated—like a high-end cyberpunk collectible card.",
    "style": {
        "lighting": "Neon glow, soft reflections",
        "font": "Modern sans-serif, clean and minimal",
        "layout": "Centered, structured like a digital collectible card",
        "materials": "Glass, holographic plastic, glowing metal edges"
    },
    "parameters": {
        "logo": "Tesla logo",
        "ticker": "TSLA",
        "company_name": "Tesla Inc.",
        "card_number": "#0006",
        "revenue": "$96.8B",
        "year": "2025",
        "colors": ["red", "white", "dark gray"]
    },
    "medium": "3D render, high-resolution digital art",
    "size": "1080px by 1080px"
}

sword_1 = {
  "prompt": "A premium fantasy loot sprite of an ornate {{subclass}} {{item_type}} with {{element}} element and {{rarity}} rarity, rendered for a game inventory icon. Emphasize a {{silhouette_class}} silhouette, {{material_set}}, and subtle emissive runes. Orientation: {{orientation}}; scale in frame: {{scale_in_frame}}. Include {{attachments}}; sockets: {{socket_count}}. VFX: {{vfx_trail}} at intensity {{vfx_intensity}} with {{particle_style}} particles; overlay style: {{elemental_overlay_style}}.",
  "style": {
    "render_style": "flat_vector_render",
    "outline_style": "inner_outline",
    "shading_model": "flat",
    "lighting_direction": "top_left",
    "lighting_intensity": 0.7
  },
  "parameters": {
    "item_type": "sword",
    "subclass": "longsword",
    "rarity": "epic",
    "element": "fire",
    "silhouette_class": "ornate",
    "material_set": ["polished_steel","gold_inlay","leather_wrap"],
    "wear_level": "light_wear",
    "palette": ["#F5E6C8","#C7A566","#873D1B","#FF8A00","#2B2B2B"],
    "palette_size_limit": 16,
    "orientation": "angled_3q",
    "scale_in_frame": 0.88,
    "attachments": ["gem_socket","runes"],
    "socket_count": 1,
    "ornament_density": 0.6,
    "vfx_trail": "none",
    "vfx_intensity": 0.5,
    "particle_style": "none",
    "elemental_overlay_style": "none"
  },
  "export": {
    "canvas_size": {"w":128,"h":128}, 
    "padding_px": 6,
    "background":"transparent", 
    "shadow_style":"none", 
    "export_format":"svg", 
    "atlas_tag":"none"
    },
  "repro": { 
    "style_preset":"loot_v1",
    "model_tag":"gpt-5",
    "lora_set":["ornate_metals_v2","arcane_runes_v1"],
    "seed":381274,
    "variation_strength":0.25,
    "version":"1.3.0" 
    }
}

sword_2 = {
  "prompt": "A premium fantasy loot sprite of an ornate {{subclass}} {{item_type}} of {{element}} element and {{rarity}} rarity, rendered for a game inventory icon. Emphasize a {{silhouette_class}} silhouette, {{material_set}}, and subtle emissive runes. Orientation: {{orientation}}; scale in frame: {{scale_in_frame}}. Include {{attachments}}; sockets: {{socket_count}}.",
  "style": {
    "render_style": "flat_vector_render",
    "outline_style": "inner_outline",
    "shading_model": "flat",
    "lighting_direction": "top_left",
    "lighting_intensity": 0.7
  },
  "parameters": {
    "item_type": "sword",
    "subclass": "longsword",
    "rarity": "epic",
    "element": "fire",
    "silhouette_class": "ornate",
    "material_set": ["polished_steel","gold_inlay","leather_wrap"],
    "wear_level": "light_wear",
    "palette": ["#F5E6C8","#C7A566","#873D1B","#FF8A00","#2B2B2B"],
    "palette_size_limit": 16,
    "orientation": "angled_3q",
    "scale_in_frame": 0.88,
    "attachments": ["gem_socket","runes"],
    "socket_count": 1,
    "ornament_density": 0.6
  },
  "export": {
    "canvas_size": {"w":128,"h":128}, 
    "padding_px": 6,
    "background":"transparent",
    "export_format":"svg"
    },
  "repro": { 
    "style_preset":"loot_v1",
    "model_tag":"gpt-5",
    "lora_set":["ornate_metals_v2","arcane_runes_v1"],
    "seed":381274,
    "variation_strength":0.25,
    "version":"1.3.0" 
    }
}

# Source: https://x.com/IamEmily2050/status/1977075634536169827
woman_mommy = {
    "style": "smartphone_selfie_low_light_high_contrast",
    "image_description": {
      "subject": {
        "type": "Person",
        "gender": "Female",
        "age_appearance": "Young Adult (early 20s)",
        "ethnicity_appearance": "East Asian",
        "complexion": {
          "tone": "Extremely pale, fair.",
          "texture": "Smooth, flawless, matte finish."
        },
        "hair": {
          "color": "Intense platinum blonde. Appears almost white in direct light, with subtle silvery or pale lavender undertones visible in the shadows.",
          "style": "Long and straight, voluminous, flowing over the shoulders and chest.",
          "bangs": "Full, straight-cut fringe (bangs) ending just above the eyelashes.",
          "texture": "Soft, slightly wispy, highly reflective of light."
        },
        "facial_features": {
          "eyes": {
            "size": "Large and prominent (doe-eyed).",
            "color": "Cool-toned grey or deep blue-grey. Enhanced by colored contact lenses with a defined limbal ring.",
            "makeup": "Dramatic and precise. Thick black eyeliner on the upper lid with a sharp wing. Very long, dense, and voluminous false eyelashes on both upper and lower lashes. Defined 'aegyo-sal' (under-eye area emphasized with subtle highlight/shimmer).",
            "eyebrows": "Relatively straight, groomed, and filled in softly."
          },
          "nose": "Small, slim bridge, defined tip, highlighted along the bridge.",
          "lips": {
            "shape": "Full, plump, well-defined cupid's bow.",
            "state": "Slightly parted.",
            "color": "Soft, glossy muted-pink or peach lip tint."
          }
        },
        "expression": "Neutral, direct, slightly sultry gaze into the camera lens."
      },
      "attire_and_accessories": {
        "clothing": {
          "top": "Black strapless top (tube top or dress). Shoulders and clavicle are bare.",
          "details": "The fabric is deep black. Upon close inspection, a subtle, darker lace or embroidered pattern is visible on the bodice area.",
          "bottoms": "Black material visible on the thigh in the lower-left corner (suggesting shorts, skirt, or thigh-highs)."
        },
        "jewelry": [
          {
            "type": "Earring",
            "location": "Left ear",
            "description": "A very large, thin, metallic silver hoop earring."
          },
          {
            "type": "Necklace",
            "description": "Worn on a thin dark cord or chain.",
            "pendant": "A prominent, ornate silver cross. The pendant has a stylized, gothic or fantasy design with flared, pointed ends. The surface is intricate and catches the light, suggesting embedded crystals or multifaceted metalwork."
          }
        ]
      },
      "pose_and_composition": {
        "type": "Selfie",
        "orientation": "Portrait",
        "angle": "Slightly high angle.",
        "framing": "Close-up, tightly framed on the head, shoulders, and upper torso.",
        "pose": "Subject is reclining or seated. Her right arm is extended forward towards the camera (holding the device), creating a forced perspective where the arm and shoulder are prominent in the lower right foreground."
      },
      "environment_and_lighting": {
        "environment": "Indoor, very dark, suggesting nighttime or a dimly lit room.",
        "lighting": {
          "source": "Frontal, direct lighting (likely from the phone screen, flash, or ring light).",
          "effect": "High contrast. Illuminates the face and hair brightly against the dark background. Creates bright catchlights in the eyes. Soft shadows define the facial structure."
        },
    }
  }
}

# Source: https://x.com/karatademada/status/1976950313505423477
curly_girl = {
  "title": "Warm night street portrait with vintage flash aesthetic",
  "style": "Candid nightlife portrait with early-2000s Y2K fashion and Polaroid-film texture. Warm tones, visible grain, and slight color shift for an authentic analog look. Direct flash lighting with deep contrast and spontaneous energy.",
  "subject": {
    "category": "human",
    "gender_presentation": "female",
    "age_bracket": "young_adult",
    "ethnicity": "biracial",
    "skin_tone": "warm golden-caramel",
    "hair": {
      "texture": "curly",
      "length": "medium-long",
      "style": "naturally curly, slightly messy, loose strands framing face and falling over shoulders"
    },
    "face": {
      "expression": "eyes closed, soft relaxed lips, calm confidence, serene and natural",
      "makeup": "dewy skin, warm highlights on cheekbones, subtle eyeliner, glossy lips"
    },
    "body": {
      "pose": "seated or leaning back slightly against railing, torso turned 3/4 to camera, head tilted back gently",
      "gesture": "right hand brushing shoulder or collarbone, left hand resting near shorts waistband"
    }
  },
  "wardrobe": {
    "top": "black lace bralette (tasteful, fashion-forward)",
    "outerwear": "black leather jacket worn loose and off-shoulder",
    "bottoms": "light blue denim shorts, slightly frayed hem, mid-rise fit",
    "accessories": [
      "brown leather belt",
      "small keychain or charm hanging from belt loop",
      "gold or silver small hoop earrings",
      "thin gold necklace"
    ]
  },
  "environment": {
    "setting": "nighttime New York City street or elevated walkway",
    "background": "rusted metal railings with vertical bars, dim warm city lights and bokeh in background",
    "lighting_condition": "low-light environment, single flash source"
  },
  "camera": {
    "framing": "medium close-up (waist to head)",
    "angle": "slightly above subject, tilted composition for natural feel",
    "focal_length": "35mm equivalent",
    "depth_of_field": "shallow, soft background blur",
    "film_type": "warm color negative film (Kodak Gold 200 aesthetic)"
  },
  "lighting": {
    "key": "direct on-camera flash",
    "fill": "none",
    "temperature": "warm 4200K",
    "notes": "slight overexposure on skin for flash realism; hard shadow behind railing for authentic snapshot effect"
  },
  "composition": {
    "framing_notes": "tight crop, include shorts line and right hand gesture, eyes closed and head slightly tilted back",
    "pose_notes": "relaxed body language with natural flow",
    "background_blur": "subtle bokeh on street lights"
  },
  "colors": {
    "palette": "warm amber tones, soft golden skin, faded blue denim, black leather, muted dark background",
    "contrast": "medium-high",
    "saturation": "slightly increased for warmth"
  },
  "postprocessing": {
    "look": "vintage film snapshot",
    "grain": "medium grain visible throughout image",
    "vignette": "gentle and warm",
    "white_balance": "flash/daylight with slight yellow tint",
    "exposure": "slightly overexposed highlights on skin",
    "contrast": "high microcontrast for flash pop",
    "color_grade": "warm golden cast with magenta shadows for nostalgic feel",
    "texture": "light film halation and fine dust specks"
  },
  "output": {
    "aspect_ratio": "4:5",
    "resolution": "1080x1350",
    "render_intent": "photo",
    "color_profile": "sRGB"
  },
  "negatives": [
    "no nudity",
    "no extreme makeup",
    "no cinematic lighting",
    "no other people",
    "no smile or direct eye contact",
    "no heavy retouching",
    "no cold color tones"
  ]
}