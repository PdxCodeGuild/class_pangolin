'''
 02_jackalope.py
 written by 
 Rhi, Nathan, Brendan, Jeff
'''
import random
import string
#jack_list = []
gen = ['m', 'f']

#jack = {'name': '', 'age': 0, 'gen': '', 'p': False}
jack_list = [{'name': 'adam', 'age': 0, 'gen': 'm', 'p': False}, {'name': 'eve', 'age': 0, 'gen': 'f', 'p': False}]
yr = 0

def newjack(jack_list):
    jack_list.append({'name': random.choice(string.ascii_lowercase)*3, 'age': 0, 'gen': random.choice(gen), 'p': False})
    return jack_list
# print(newjack(jack_list))
while len(jack_list) < 1000:
    yr +=1
    # for i in range(len(jack_list)):
        # newjack(jack_list) * i
    for i in range(len(jack_list)):
        jack_list[i]['age'] += 1
        if jack_list[i]['age'] in range(4,9) and jack_list[i]['gen'] == 'f':
            
                         
            newjack(jack_list) 
        for i in reversed(range(len(jack_list))):
            if jack_list[i]['age'] == 11:
                jack_list.pop(i)

print(jack_list)



print(yr)
print(len(jack_list))
