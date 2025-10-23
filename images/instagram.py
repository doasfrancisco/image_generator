post_2 = {
  "prompt": "A detailed portrait of {{main_subject}} playing an RPG-style game on his phone in {{location}} while sitting on a chair and having his laptop next to him.",
  "style": {
    "lighting": "orange evening sunlight"
  },
  "parameters": {
    "main_subject": "an indian man",
    "location": "home office",
    "mood": "playful and cinematic"
  },
  "medium": "photorealistic 3D render or high-resolution digital painting",
  "size": "1080x1350"
}

# Reference image: https://www.instagram.com/p/DPoJka9D4-z/
location_asset = {
    "prompt": "A {{render_style}}-style {{shading_model}} illustration featuring a {{location}}, the background is dark with hints of a desk lamp and wall art.",
    "style": {
        "render_style": "pixar_style_3d",
        "shading_model": "pbr_3d",
        "lighting": "soft and warm",
        "lighting_intensity": 0.7
    },
    "parameters": {
        "orientation": "front-facing",
        "location": "streamer room with black comfy office chair, microphone and computer",
        "palette": ["#0e0506","#56201a","#d12b2a", "#ba8477"],
        "palette_size_limit": 8
    },
    "export": { 
        "canvas_size": "1024x1024", 
    }
}

# Reference image: https://www.instagram.com/p/DPoJka9D4-z/
asset_1 = {
    "prompt": "A {{render_style}}-style {{shading_model}} illustration featuring a {{main_subject}} with short, textured hair, smiling while sitting in {{location}}. {{main_subject}} wears a t-shirt, and the background is dark with hints of a desk lamp and wall art.",
    "style": {
        "render_style": "pixar_style_3d",
        "shading_model": "pbr_3d",
        "lighting": "soft and warm",
        "lighting_direction": "from the left side",
        "lighting_intensity": 0.7
    },
    "parameters": {
        "main_subject": "a young white male character",
        "orientation": "front-facing",
        "location": "streamer room with microphone and computer",
        "palette": ["#0e0506","#56201a","#d12b2a", "#ba8477"],
        "palette_size_limit": 8,
        "scale_in_frame": 0.3,
    },
    "export": { 
        "canvas_size": "1024x1024", 
        "padding_px": 6, 
        "background": "transparent" 
    }
}