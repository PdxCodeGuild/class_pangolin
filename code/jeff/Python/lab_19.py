#lab_19.py
#blackjack advice - 'codey' version
#Jeff Smith
#
#
#     Less than 17, advise to "Hit"
#     Greater than or equal to 17, but less than 21, advise to "Stay"
#     Exactly 21, advise "Blackjack!"
#     Over 21, advise "Already Busted"

cards = {'a': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '1': 10, 'ten': 10, 'j': 10, 'q': 10, 'k': 10}
def card_eval(card1, card2, card3):
    tot = cards[card1] + cards[card2] + cards[card3]
    if tot < 17:
        print('Hit.')
    elif tot in range(17, 21):
        print('You should stay.')
    elif tot == 21:
        print('Blackjack. You win!')
    elif tot > 21:
        print('Bust. You lose!')

one = input('Enter your 1st card(A, 2-10, J, Q, K): ').lower()
a = one[0]
two = input('Enter your 2nd card(A, 2-10, J, Q, K): ').lower()
b = two[0]
three = input('Enter your 3rd card(A, 2-10, J, Q, K): ').lower()
c = three[0]
print(card_eval(a, b, c))

'''
cards = {'a': 1, '2': 2, 'two': 2, '3': 3, 'three': 3, '4': 4, 'four': 4, '5': 5, 'five': 5, '6': 6, 'six': 6, '7': 7, 'seven': 7, '8': 8, 'eight': 8, '9': 9, 'nine': 9, '1': 10, 'ten': 10, 'j': 10, 'q': 10, 'k': 10}
'''