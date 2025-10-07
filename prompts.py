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