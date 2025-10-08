# What is this?

A free notebook and collection of JSON prompts for image generation I'm building while making my app. Check prompts in `prompts.py`

### Example:

```
{
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
```

## Structure
subject -> lighting -> background -> mood -> camera behavior.


## Questions
- What is cel?

    It means simulating that old 2D hand-painted look inside 3D graphics. Surfaces are colored with flat, uniform tones instead of smooth gradients.Shadows appear as sharp bands. Outlines are often drawn around the geometry to mimic ink lines.
- What is outline style?

    In stylized art (especially “cel” or “toon” styles), outlines help define shapes and make objects readable at small sizes.
- What is shading model?

    The algorithm or “lighting logic” used to compute how light interacts with the surface.

    This controls how light → shadow transitions behave — from realistic to purely stylized.

- What is angled 3q?

    Three-quarter view” — also written as 3/4 view or 3q angle — is a slightly rotated perspective where you can see both the front and a bit of the side (and sometimes a hint of the top).
    
    Render the loot at a slight diagonal angle so it looks 3D and dynamic, not flat.

- What is VFX trail?

    The visual trail effect the item emits when moving or floating — often used for magical or elemental items.

- What is particle_style?

    Defines the shape and behavior of small floating particles around or trailing the item.
    These support the VFX, adding life and motion.

- What is elemental overlay?

    Controls where the elemental energy or magical aura appears on the item.
    Basically: which parts "glow" or "charge up".

- What is shadow_style?

    Controls how shadows are rendered beneath or around the item when exporting the image.

- What is atlas_tag?

    A label or category name that defines which texture atlas or export group this sprite belongs to.
    Example: "weapons_tier3"

- What is repro?

    When you're generating thousands of loot sprites, every image depends on a specific model or checkpoint, version of your prompt schema, LoRA or style modules loaded, and random seed.

    If you don't record those, you'll never be able to reproduce an identical output later.
    So "repro" = the recipe you need to re-bake the exact same image.



## ✨ Pro Tip

Keep a style_preset library that groups render styles + lighting + material + palette choices, like:

```
"style_preset": "loot_v1_dark_fantasy",
"render_style": "hand_painted_fantasy",
"lighting": "volumetric warm candlelight",
"materials": "aged metal, dragonbone, glowing runes"
```


## Additional Notes
style, 
if adding text use font.
apparently, always use lighting?
layout maybe for structuring single object