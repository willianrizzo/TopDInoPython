DINO_NAMES = (
    "Alossauro",
    "Pterodatilo",
    "Raptor", 
    "Godzilla",
    "Trex",
    "Carnotauro"
)

def generate_deck():
    dino_cards =[]

    for dino_name in DINO_NAMES:
        dino_card = {
            "name": dino_name,
            "strengh":10,
            "agility": 12.2,
            "height": 5.22,
        }

        dino_cards.append(dino_card) #adciona valores nas listas
    return dino_cards
