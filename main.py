import json
import prompts
import copy

elements = ["ice", "electric", "water", "holy", "dark", "earth", "wind"]
# weapon_types = ["sword", "dagger", "bow", "mace", "axe", "hammer"]
# weapon_types = ["sword"]


element_colors = {
    "ice": ["#E6F7FF", "#A3D9FF", "#6BB8E8", "#00A8FF", "#1C3A47"],
    "electric": ["#FFFACD", "#FFE55C", "#FFC800", "#9D00FF", "#1A1A2E"],
    "water": ["#B3E5FC", "#4FC3F7", "#0288D1", "#01579B", "#263238"],
    "holy": ["#FFFEF7", "#FFE082", "#FFF59D", "#FFD700", "#424242"],
    "dark": ["#4A4A4A", "#2E2E2E", "#1A1A1A", "#8B00FF", "#000000"],
    "earth": ["#D7CCC8", "#A1887F", "#6D4C41", "#4E342E", "#1B5E20"],
    "wind": ["#F1F8E9", "#C5E1A5", "#9CCC65", "#7CB342", "#546E7A"]
}

weapon_subclasses = {
    "sword": "longsword",
    "dagger": "stiletto",
    "bow": "longbow",
    "mace": "war mace",
    "axe": "battle axe",
    "hammer": "war hammer"
}

weapon_materials = {
    "sword": ["polished_steel", "gold_inlay", "leather_wrap"],
    "dagger": ["Damascus_steel", "leather_grip", "silver_pommel"],
    "bow": ["yew_wood", "silk_string", "bone_limbs"],
    "mace": ["iron_head", "oak_shaft", "bronze_spikes"],
    "axe": ["forged_steel", "hardwood_handle", "brass_rivets"],
    "hammer": ["tempered_iron", "reinforced_oak", "steel_bands"]
}

weapon_attachments = {
    "sword": ["gem_socket", "runes"],
    "dagger": ["runes"],
    "bow": ["quiver", "scope"],
    "mace": ["chain", "runes"],
    "axe": ["runes", "edge_serration"],
    "hammer": ["runes", "impact_plates"]
}

combinations = []

for element in elements:
    for weapon_type in weapon_types:
        temp_prompt = copy.deepcopy(prompts.sword_2)

        temp_prompt["parameters"]["item_type"] = weapon_type
        temp_prompt["parameters"]["subclass"] = weapon_subclasses[weapon_type]
        temp_prompt["parameters"]["element"] = element
        temp_prompt["parameters"]["palette"] = element_colors[element]
        temp_prompt["parameters"]["material_set"] = weapon_materials[weapon_type]
        temp_prompt["parameters"]["attachments"] = weapon_attachments[weapon_type]

        if weapon_type != "sword":
            temp_prompt["parameters"].pop("socket_count", None)

        combinations.append(temp_prompt)

# print(json.dumps(combinations, indent=2))

with open("temp_prompt.py", "w") as f:
    f.write("# Generated weapon combinations\n")
    f.write("# Total combinations: {}\n\n".format(len(combinations)))
    f.write("combinations = [\n")
    for i, combo in enumerate(combinations):
        f.write("    # Combination {}: {} - {}\n".format(i+1, combo["parameters"]["element"], combo["parameters"]["item_type"]))
        f.write("    " + json.dumps(combo, indent=4).replace("\n", "\n    ") + ",\n")
    f.write("]\n")

print(f"Generated {len(combinations)} combinations ({len(elements)} elements x {len(weapon_types)} weapon types)")
print(f"Saved to temp_prompt.py")