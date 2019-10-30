'''
 00_jackalope.py
 written by 
 Rhi, Nathan, Brendan, Jeff
'''
jack = [0, 0]

yr = 0
while len(jack) < 1000:
    yr +=1
    for i in range(len(jack)):
        jack[i] += 1
    for i in jack:
        if i in range(4,9):
            jack.append(0)
    for i in reversed(range(len(jack))):
        if jack[i] == 11:
            jack.pop(i)
print(yr)
print(len(jack))
