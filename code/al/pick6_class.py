# pick6_class.py
import random
class Ticket:
    cost = 2
    win_amounts = (0, 4, 7, 100, 50000, 1000000, 25000000)

    def __init__(self):
        self.nums = []
        for i in range(6):
            self.nums.append(random.randint(0, 99))
    
    def __eq__(self, in_ticket):
        for i in range(len(self)):
            if self[i] != in_ticket[i]:
                return False
        return True

    def __getitem__(self, index):
        return self.nums[index]

    def __len__(self):
        return len(self.nums)

    def check(self, in_ticket):
        matches = 0
        for i in range(len(self)):
            if self[i] == in_ticket[i]:
                matches += 1
        return matches
    
    @staticmethod
    def winnings(matches):
        #win_amounts = (0, 4, 7, 100, 50000, 1000000, 25000000)
        return Ticket.win_amounts[matches] - Ticket.cost
        
winning_ticket = Ticket()
total_matches = 0
winnings_num = 0
for i in range(100000):
    bought_ticket = Ticket()
    matches = winning_ticket.check(bought_ticket)
    total_matches += matches
    winnings_num += Ticket.winnings(matches)
print(total_matches)
print(winnings_num)

'''
>>> winning_ticket = Ticket()
>>> bought_ticket = Ticket()
>>> winning_ticket[0]
72
>>> winning_ticket[5]
81
>>> winning_ticket[6]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/intro/Desktop/pangolin/pick6_class.py", line 19, in __getitem__
    return self.nums[index]
IndexError: list index out of range
>>> winning_ticket == bought_ticket
False
>>> len(winning_ticket)
6
>>> winning_ticket.check(bought_ticket)
2
>>> Ticket.winnings(2)
5
>>> 
'''