# Initially the program will pick 6 random numbers as the 'winner'. Then try playing pick6 100,000 times, with the ticket cost and payoff below.

import random


def generate_ticket():
    ticket_list = []
    for y in range(6):
        ticket_numbers = random.randint(0, 99)
        ticket_list.append(ticket_numbers)
    return ticket_list


ticket_list = []
winning_list = []
user_ticket = []
count = 0
ticket_tracker = []
ticket_zip = []
result_zip = []
result = []
# matches = 0
dollar_tracker = 0
expenses_tracker = 0
earnings_tracker = 0
roi = 0

# Generates the winning ticket number
for i in range(6):
    winning_numbers = random.randint(0, 99)
    winning_list.append(winning_numbers)

# Generates a list of lists appends the generated user ticket from the generate ticket function.
for y in range(100000):
    dollar_tracker -= 2
    expenses_tracker = dollar_tracker
    matches = 0
    ticket = generate_ticket()
    # ticket_list.append(generate_ticket())
    # ticket_numbers = random.randint(0, 99)
    # ticket_list.append(ticket_numbers)
    # for ticket in ticket_list:
    print(ticket)
    ticket_zip = zip(ticket, winning_list)
    result = list(ticket_zip)
    # print(result)
    for x, y in result:
        matches_list = []
        if x == y:
            matches += 1
        else:
            continue
    # print(matches)
    if matches == 1:
        dollar_tracker += 4
        earnings_tracker += 4
    elif matches == 2:
        dollar_tracker += 7
        earnings_tracker += 7
    elif matches == 3:
        dollar_tracker += 100
        earnings_tracker += 100
    elif matches == 4:
        dollar_tracker += 50000
        earnings_tracker += 50000
    elif matches == 5:
        dollar_tracker += 1000000
        earnings_tracker += 1000000
    elif matches == 6:
        dollar_tracker += 25000000
        earnings_tracker += 25000000
    roi = (earnings_tracker - expenses_tracker) / expenses_tracker
    roi = round(roi, 2)
    print(dollar_tracker)

ticket_tracker = []

print(f"The Winning Numbers are: {winning_list}")
print(f"You have ${dollar_tracker} dollars!")
print(f"The earnings were ${earnings_tracker}")
print(f"The expenses were ${expenses_tracker}")
print(f"The ROI is ${roi}")
