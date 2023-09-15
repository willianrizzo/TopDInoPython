from top_dino.deck import *

def play() -> None:
    #1. gerar o baralho
    dino_deck = generate_deck()
    # print(dino_deck)

    #2. embaralhar as cartas
    # print(split_deck(dino_deck))
    p1_deck, p2_deck = split_deck(dino_deck)

    #3. gerar relatiorio de batalha

    p1_score = 0
    p2_score = 0

    for index ,p1_card in enumerate(p1_deck):
       p2_card = p2_deck[index]
       attr_compare = get_random(p1_card)
       print(attr_compare)

       print(f"p1 card -> {p1_card}")
       print(f"p2 card -> {p2_card}")
       print(f"attr_compare -> {attr_compare} ")

    if p1_card[attr_compare] > p2_card[attr_compare]:
       p1_score += 1
       print(f'{p1_card["name"]} Wins')
    elif p1_card[attr_compare] < p2_card[attr_compare]:
       p2_score +=1
       print(f'{p1_card["name"]} Wins')
    else:
       print("Draw")

#--------------------------------------- fim do for
    print("-"*20)

    if p1_score > p2_score:
              print("player 1 Wins")
    elif p1_score < p2_score:
              print("player 2 wins")
    else: print("Draw")