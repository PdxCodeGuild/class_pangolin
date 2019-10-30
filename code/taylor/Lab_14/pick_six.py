import random

a, b, c, d, e, f = 0, 0, 0, 0, 0, 0
# m1, m2, m3, m4, m5, m6 = a *4,b * 7,c * 100,d * 50000,e * 1000000,f * 25000000

def calc_winnings(a, b, c, d, e, f):
    total = sum([a * 4, b * 7, c * 100, d * 50000, e * 1000000, f * 25000000])
    return total

# Generates a random list of 6 integers between 1 & 99 inclusive
def get_six():
    six_lst = []
    for n in range(1, 7):
        six_lst.append(random.randint(1, 99))
    return six_lst
budget = 0
i = 0
while i < 10:

    mtchs = len(set(get_six()) & set(get_six()))
  
    if mtchs == 1:
        a += 1
    elif mtchs == 2:
        b += 1  
    elif mtchs == 3:
        c += 1
    elif mtchs == 4:
        d += 1
    elif mtchs == 5:
        e += 1
    elif mtchs == 6:
        f += 1
    i += 1
    budget -= 1

print("\nTotal Winnings > $",calc_winnings(a, b, c, d, e, f))
print("Budget > $", budget)
print(f"ROI > {(calc_winnings(a, b, c, d, e, f) - budget) / budget }%")








