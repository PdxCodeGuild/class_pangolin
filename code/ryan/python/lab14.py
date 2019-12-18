import random
balance = 0

def pick_6():
    nums = []
    for i in range(6):
        nums.append(random.randint(1, 101))
    return nums

def num_matches():
    matches = 0
    for i in range(6):
        if winning[i] == my_ticket[i]:
            matches += 1
    return matches

i = 1
while i <= 100000:
    winning = pick_6()
    my_ticket = pick_6()
    matches = num_matches()
    balance -= 2
    if matches == 1:
        balance += 4
    elif matches == 2:
        balance += 7
    elif matches == 3:
        balance += 100
    elif matches == 4:
        balance += 50000
    elif matches == 5:
        balance += 1000000
    elif matches == 6:
        balance += 25000000
    i += 1

print(f"Your balance is:  ${balance}")
