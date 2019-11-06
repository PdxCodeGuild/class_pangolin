#MobLab2: Hangman 
#Austen, Brandon, Franki, Rhi

import random
import string
import pillow_talk

word_list = []
with open('english.txt', 'r') as file:
    file = file.read().split("\n")
    for word in file:
        if len(word) >= 5:
            word_list.append(word)

print("Welcome to Hangman!")
print("Enter '1' to quit at any time")
        
def game():        
    game_word = random.choice(word_list)
    #print(game_word)

    word = list(game_word)
    redacted_word = []
    guessed_letters = []
    guesses = 10
    for letter in word:
        redacted_word.append('_')
    replay = "yes"
    while replay == "yes":
        print(' '.join(redacted_word))
        guess = input("Guess a letter. ").lower()
        if guess == "exit" or guess == '1':
            print("Sayonara!")
            quit()
        elif guess in guessed_letters:
            print("You already guessed that!")
            print(guessed_letters)
            continue
        elif guess not in string.ascii_lowercase:
            print("Your guesses need to be a single letter please.")
        elif len(guess) > 1:
            print("Your guesses need to be a single letter please.") 
        else:
            correct_guesses = 0
            for i in range(len(word)):
                if word[i] == guess:
                    redacted_word[i] = guess
                    correct_guesses += 1
            if correct_guesses == 0:
                print(f"Sorry, there's no {guess}.")
                guesses -=1
                pillow_talk.picture(guesses)
                print(guessed_letters)
                print(f"You have {guesses} guesses left.\n")
            elif correct_guesses == 1:
                print(f"There's one {guess}.\n")
            else:
                print(f"There are {correct_guesses} {guess}'s.\n")

        if guesses == 0:
            print(f"I'm sorry, you lose! The word was {game_word}")
            pillow_talk.picture(guesses)
            break
        elif redacted_word == word:
            print(' '.join(redacted_word))
            print("You win!!!!")
            break
        guessed_letters.append(guess)
        

game()

while True:
    replay = input("Do you want to play Hangman? yes or no\n>: ").lower()
    if replay in ["y", "yes"]:
        game()
    else:
        print("Sayonara!")
        quit()
