import random #biblioteca feita para randomizar 

DINO_NAMES = (
    "Alossauro",
    "Pterodatilo",
    "Raptor", 
    "Godzilla",
    "Trex",
    "Carnotauro"
)

def generate_deck() -> list[dict]:
    # dino_cards =[]

    # for dino_name in DINO_NAMES: 
    #criando um dino card para cada nome no Dino_Names
    #     dino_card = {
    #         "name": dino_name,
    #         "strength":random.randint(1,10), #definindo que sera random de 1 a 10
    #         "agility": round(random.uniform(0, 10),1 ),
    #         "height": round(random.uniform(0, 10), 2), #uniform serve para randomizar floats, round arredonda casas
    #     }

    #     dino_cards.append(dino_card) #adciona valores nas listas

    dino_cards = [
        {
            "name": dino_name,
            "strength":random.randint(1,10), #definindo que sera random de 1 a 10
            "agility": round(random.uniform(0, 10),1 ),
            "height": round(random.uniform(0, 10), 2), #uniform serve para randomizar floats, round arredonda casas
        }
        for dino_name in DINO_NAMES
    ] 
    
    return dino_cards

def split_deck(deck:list[dict]):
    random.shuffle(deck)
    