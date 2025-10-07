render_styles = [
    # 1. Pixel / Low-Res Art
    "pixel_art",
    "hd_pixel_art",
    "iso_pixel_art",
    "voxel_render",

    # 2. Painted / Illustration Styles
    "hand_painted_fantasy",
    "digital_painting",
    "oil_paint_render",
    "matte_painting",
    "storybook_illustration",
    "concept_art_render",
    "stylized_paint_render",

    # 3. 3D and Material-Driven
    "pbr_3d_render",
    "toy_plastic_render",
    "miniature_model_render",
    "clay_render",
    "photorealistic_render",
    "cinematic_3d_render",
    "holographic_3d_render",

    # 4. Stylized / Artistic Abstractions
    "cel_shaded_render",
    "flat_vector_render",
    "low_poly_render",
    "neon_outline_render",
    "line_art_render",
    "posterized_render",

    # 5. UI / Iconic Rendering
    "game_icon_render",
    "collectible_card_render",
    "inventory_ui_flat",
    "vector_icon_render",

    # 6. Experimental / Hybrid Styles
    "holographic_card_render",
    "metallic_emboss_render",
    "rune_etched_render",
    "biotech_render",
    "void_energy_render",
    "animated_emissive_render",

    # 7. Cross-Media / Niche Looks
    "clay_stopmotion_render",
    "lego_brick_render",
    "papercraft_render",
    "origami_render",
    "pixel_ink_render",
    "vintage_gameboy_render",
    "retro_ps1_render",
]

outline_styles = [
    "none",  # No outline; pure color or realistic shading. Used in realistic renders.
    "1px_dark",  # A thin, dark contour (usually black or dark gray) around the object. Classic pixel-art or anime look.
    "inner_outline",  # The outline sits just inside the edge; gives a crisp inlay look. Used in icons and collectible cards.
    "colored_edge",  # Outline takes a darker tint of the object's base color. Common in cel-shaded 3D (e.g. Genshin Impact).
    "glow_outline",  # Outline glows instead of darkens; used for magical/epic loot. Fire, lightning, or arcane items.
    "double_outline",  # Two bands (light + dark); adds stylized thickness or embossed look. Seen in UI icons for readability.
]

shading_models = [
    "toon",  # Two or three flat color bands for light, midtone, shadow. Creates cartoon/cel look. Stylized / readable game icons.
    "soft",  # Smooth gradient transitions between light and dark. Natural or digital painting look.
    "pbr",  # Physically Based Rendering - Simulates real-world materials: reflection, roughness, metalness. Realistic 3D renders.
    "flat",  # No shading at all — pure flat colors per face or pixel. Vector, flat UI icons, pixel art.
    "rim_heavy",  # Emphasizes rim lighting (bright edge light), dark center. Magical / sci-fi loot glow.
    "diffuse_only",  # Soft shadows, no specular highlights. Matte or painterly items.
    "gradient_map",  # Uses color gradients instead of calculated light. Stylized 2D look, used in retro art.
]

orientation = [
    "front",  # Flat, orthographic, used for UI icons
    "profile_left",  # Pure side-on, good for pixel weapons
    "profile_right",  # Pure side-on, good for pixel weapons
    "top_down",  # Used in isometric maps
    "isometric",  # 3D but with consistent grid projection
    "angled_3q",  # Cinematic, standard hero angle
    "rear_3q",  # From behind, used for mounts or vehicles
    "dynamic_tilt",  # Slightly rotated, dramatic presentation shot
]

silhouette_classes = [
    "simple",  # Basic geometric shapes. Common / low-tier loot
    "sleek",  # Smooth, minimal. Modern, lightweight gear
    "bulky",  # Heavy, massive proportions. Hammers, armor, tanks
    "ornate",  # Decorative, layered, with flourish. Epic or legendary loot
    "spiky",  # Aggressive, jagged shapes. Dark or demonic items
    "organic",  # Curved, flowing like bone or vines. Nature / beast themes
]

wear_level = [
    "mint",  # Brand new, shiny, no scratches
    "light_wear",  # Slight edge scuffs, some patina
    "battleworn",  # Dents, scratches, maybe chipped
    "ancient_relic",  # Rusted, cracked, partially broken
    "ruined",  # Nearly destroyed, corroded surfaces
]

vfx_trails = [
    "none",  # No trail, static item
    "flame",  # Follows with fire or ember streaks
    "smoke",  # Soft, dissipating smoke trail
    "spark",  # Electric sparks following motion
    "aura",  # Soft glowing outline with particles
    "frost",  # Misty vapor trail
    "void",  # Black energy distortion or dark smoke
]

particle_styles = [
    "embers",  # Small glowing orange dots (fire)
    "snow",  # White drifting flakes (ice)
    "spores",  # Floating organic motes (nature / poison)
    "dust",  # Soft brownish haze (earth / aged)
    "sparkles",  # Bright white glints (holy / rare)
    "mist",  # Low-opacity smoke particles
    "stars",  # Shimmering points (cosmic / divine)
]

elemental_overlay_styles = [
    "none",  # No overlay; material-only look
    "edge_rim",  # Glow or energy around outer edges (like a lightsaber edge)
    "core_glow",  # Energy radiates from the center/core or engravings
    "coating",  # Thin, full-surface magical sheen
    "pattern_runes",  # Glow follows engraved runes or patterns
    "crack_glow",  # Light leaks through cracks or damage lines
    "pulse_overlay",  # Animated pulse through the surface
    "aura_field",  # Energy field slightly detached from surface
]

shadow_styles = [
    "none",  # No shadow at all. Clean transparent sprite.
    "soft_drop",  # Soft blurred shadow offset from the object. Feels like it's floating slightly above the ground.
    "contact_only",  # Tiny, tight shadow directly under the item's base. Looks like the object is resting on a surface — no floating.
]