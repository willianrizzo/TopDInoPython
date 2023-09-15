from top_dino.deck import *

def play() -> None:
    #1. gerar o baralho
    dino_deck = generate_deck()
    print(dino_deck)

    #2. embaralhar as cartas
    p1_deck = split_deck(dino_deck)

    #3. gerar relatiorio de batalha