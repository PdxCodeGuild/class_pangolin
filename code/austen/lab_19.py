#First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K)
#figure out the point value of each card individually
#Number cards are worth their number, all face cards are worth 10
#aces are worth 1
# Less than 17, advise to "Hit"
# Greater than or equal to 17, but less than 21, advise to "Stay"
# Exactly 21, advise "Blackjack!"
# Over 21, advise "Already Busted"

#Welcome statment 
print('Welcome to the Blackjack simulator, do you have what it takes to win?')

#define the game loop
def game():

# list out valid user input operations
    playing_cards = print('Here is a list of your card choices:\n (a,2,3,4,5,6,7,8,9,10,j,q, k)')
    user_input1 = (input('What is your first number? :')) #user input 1,2,3
    user_input2 = (input('What is your second number? :'))
    user_input3 = (input('What is your third number? :'))

#dictinary for all the different numbers and there keys
    nums = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'j': 10, 'q':10, 'k':10 ,'a':1}

# adding all the values that the user inputed to get the total number 
    actual = (nums[user_input1] + nums[user_input2] + nums[user_input3])

    print (actual)

#create if statments in order to get a valid answer 
    if actual < 17:
        print ('hit')
    elif actual in range (17,21):
        print ('stay')
    elif actual == 21:
        print ('blackjack')
    else:
        actual > 21
        print ('already busted')

#create a while loop to ask the user if they want to play again 
    while True:
        ask_again= input('Would you like to try different numbers? ')
        if ask_again in ['yes','y']:
            game()
        elif ask_again in ['no', 'n']:
            print('Thank you for participating')
            break
        else:
            print ('please enter a valid option * yes or no * ')
game()


