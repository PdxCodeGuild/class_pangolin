# Taylor Rebbe
# PDX Code Guild
# Lab_19
# 10/28/2019

# User message variables
msg1 = "Enter card 1: > "
msg2 = "Enter card 2: > "
msg3 = "Enter card 3: > "

# User input variables
c_one = input(msg1).lower()
c_two = input(msg1).lower()
c_thr = input(msg1).lower()

# Function returns the card value for face and numeric cards
def c_val(c):

    if c == 'j' or c == 'q' or c == 'k':
        return 10
    elif c == 'a':
        return 1
    else:
        return int(c)

# Sums the 3 cards
c_sum = c_val(c_one) + c_val(c_two) + c_val(c_thr)
print("-----------------")
print("Card Total: ", c_sum)

# Tests card sum for condition and makes recommendation
if c_sum < 17:
    print("\nHit")
elif c_sum <= 20:
    print("\nStay")
elif c_sum == 21:
    print("\nBlackjack")
else:
    print("\nWomp waa...")
