# by casey, franki, and taylor

import random
jackalopes = [{'name': 'jack', 'age': 0, 'female': False, 'expecting': False}, {'name': 'jacqueline', 'age': 0, 'female': True, 'expecting': False}]
consonants = ['b', 'k', 'd', 'f', 'g', 'h', 'j', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
vowels = ['a', 'e', 'i', 'o', 'u']
true_false = [True, False]
def make_name():
    return str(random.choice(consonants) + random.choice(vowels) + random.choice(consonants) + random.choice(vowels) + random.choice(consonants) + random.choice(vowels))
    
def choose_sex():
    return random.choice(true_false)
def knock_up():
    return random.choice(true_false)
def make_babies():
    baby_dict = {}
    baby_dict['name'] = make_name()
    baby_dict['age'] = 0
    baby_dict['female'] = choose_sex()
    baby_dict['expecting'] = False
    return  baby_dict
    

'''
iterate through the jackalopes:
check for expecting
        if 'yes':
            make_babies()
            change 'expecting' to 'n'
check for females
    check for age 4--8
    check for male nearby
    if "yes" to both:
        change 'expecting' to 'yes'
increase age by 1
check for age 11
    if 11:
        jackalopes.remove()
count jackalopes
'''
while len(jackalopes) < 10:
    print(len(jackalopes))
    for i in range(len(jackalopes)): 
        if jackalopes[i]['expecting'] == True:
            jackalopes.append(make_babies())
            jackalopes[i]['expecting'] == False
    for i in range(len(jackalopes)):
        if jackalopes[i]['female'] == True:
            if jackalopes[i]['age'] in range (4,9):
                try:
                    neighbor1 = jackalopes[i - 1]
                    neighbor2 = jackalopes[i + 1]
                except IndexError:
                    pass
                if neighbor1['female'] == False or neighbor2['female'] == False:
                    jackalopes[i]['expecting'] = True
    for i in range(len(jackalopes)):
            jackalopes[i]['age'] += 1
    for i in range(len(jackalopes)-1, -1, -1):
            if jackalopes[i]['age'] == 11:       
                jackalopes.pop(i)
    random.shuffle(jackalopes) 
print(jackalopes)  
print(f"Number of jackalopes: {len(jackalopes)}")
print(jackalopes)
# for i in range:
#         jackalopes[index] += 1