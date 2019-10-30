def card_value(card):
    if card == "A":
        return 1
    elif card == "J" or card == "Q" or card == "K":
        return 10
    return int(card)

def advice():
    first_card = input("What is your first card?").upper()
    second_card = input("What is your second card?").upper()
    third_card = input("What is your third card?").upper()

    score = card_value(first_card) + card_value(second_card) + card_value(third_card)
    if score < 17:
        print(f"{score} Hit")
    elif 17 <= score < 21:
        print(f"{score} Stay")
    elif score == 21:
        print("Blackjack!!!!!")
    else:
        print("Busted!!!!")

advice()
