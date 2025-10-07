import json

# json_prompt = {
#     "prompt": "An icon sprite of {{main_subject}}.",
#     "parameters": {
#         "item_type": "Sword",
#         # "subtype": "Longsword",
        
#         "rarity": "Epic",
#         "element": "Fire",
#     },
#     "size": "512x512",
# }

with open('sword.json', 'r') as file:
    data = file.read()
    print(data)