print("\033c")

import json

import requests
response = requests.get("https://api.magicthegathering.io/v1/cards")

cards = json.loads(response.text)

with open("cards.json", "w") as f:
    f.write(json.dumps(cards, indent=2))
    # types = json.loads(f.read())
    # breakpoint()

print(cards)

# print(json.dumps(response.text, indent=2))

