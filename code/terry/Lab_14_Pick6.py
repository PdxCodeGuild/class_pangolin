# Initially the program will pick 6 random numbers as the 'winner'. Then try playing pick6 100,000 times, with the ticket cost and payoff below.

import random

def generate_ticket():
    ticket_list = []
    for y in range(6):
        ticket_numbers = random.randint(0, 99)
        ticket_list.append(ticket_numbers)
    return ticket_list

winning_list = []


# test_list = [55, 76, 56, 81, 57, 14]
# copy_list = test_list.copy()
# test_list2 = [55, 76, 56, 81, 14, 57]
# copy_list2 = test_list2.copy()

for i in range(6):
    winning_numbers = random.randint(0, 99)
    winning_list.append(winning_numbers)

for y in range(6):
    print(generate_ticket())




copy_winning = winning_list.copy()
#copy_ticket = ticket_list.copy()

copy_winning.sort()
#copy_ticket.sort()

# if copy_ticket == copy_winning:
#     print("These two are equal")
# else:
#     print("These are not equal")



print(f"The winning list is: {winning_list}")
#print(f"Ticket: {ticket_list}")
print()
# for z in range(6):
    #
    #     # ticket_list.append(ticket_numbers)
    #
    #     if len(winning_list) == len(ticket_list) and len(winning_list) == sum([1 for i, j in zip(winning_list, ticket_list) if i == j]):
    #         print("The lists are identical")
    #     else:
    #         print("The lists are not identical")