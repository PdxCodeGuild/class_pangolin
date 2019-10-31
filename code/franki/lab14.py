import random
def pick6():
    nums = []
    while len(nums) < 5:
        nums.append(random.randint(0, 100))
    return nums

def num_check(a, b):
    matches = 0
    for i in range(len(my_nums)):
        if my_nums[i] == winning_nums[i]:
            matches += 1
    return matches

def pay_out(c):
    if matches == 0:
        winnings = 0
    elif matches == 1:
        winnings = 4
    elif matches == 2:
        winnings = 7
    elif matches == 3:
        winnings = 100
    elif matches == 4:
        winnings = 50000
    elif matches == 5:
        winnings = 1000000
    elif matches == 6:
        winnings = 25000000
    return winnings

rounds = 0
bank = 0
total_winnings = 0
while rounds < 10000:
    bank -=2
    rounds += 1
    my_nums = pick6()
    winning_nums = pick6()
    matches = num_check(my_nums, winning_nums)
    winnings = pay_out(matches)
    bank += winnings
    total_winnings += winnings
print(f"Total winnings: ${total_winnings}")
print(f"Your bank: ${bank}")
    # print(f"Your numbers: {my_nums}")
    # print(f"Winning numbers: {winning_nums}")
    # print(f"Matches: {matches}")
    # print(f"You won: ${winnings}")
    # print(f"Your bank: ${bank}")
