#blackjack advice
card_values = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 1}

def blackjack(a, b, c):
    sum = card_values[a] + card_values[b] + card_values[c]
    if sum < 17:
        advice = f"{sum} Hit"
    elif 21 > sum >= 17:
        advice = f"{sum} Stay"
    elif sum == 21:
        advice = f"{sum} Blackjack!"
    else:
        advice = f"{sum} Busted!"
    return advice
card1 = input("What's your first card? ").upper()
card2 = input("What's your second card? ").upper()  
card3 = input("What's your third card? ").upper()
print(blackjack(card1, card2, card3))
