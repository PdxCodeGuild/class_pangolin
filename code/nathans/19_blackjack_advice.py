# 19_blackjack_advice.py
'''Objectives
1. Create dictionaries
2. Create user input
3. Add the values
4. Create if statements to determine advice
'''


### 1. dictionaries
card_value = { '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'j':10, 'q': 10, 'k': 10, 'a': 1}

### 2. user input
card_one = input("Enter first card: ")
card_two = input("Enter second card: ")
card_three = input("Enter third card: ")

### 3. add values

total_card = card_value[card_one] + card_value[card_two] + card_value[card_three]



### 4. if statements

if total_card < 17:
    print('Hit')
if total_card in range (17,21):
    print('Stay')
if total_card == 21: 
    print('Blackjack!')

if total_card > 21:
    print('Bust!! Good luck next time')








