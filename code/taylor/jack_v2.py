import random
import string

sex_lst = ['M', 'F']
stat_lst = [True, False]

consonants = ['b', 'k', 'd', 'f', 'g', 'h', 'j', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
vowels = ['a', 'e', 'i', 'o', 'u']

def make_name():
    return str(random.choice(consonants) + random.choice(vowels) + random.choice(consonants) + random.choice(vowels) + random.choice(consonants) + random.choice(vowels))

def determine_sex():
    return random.choice(sex_lst)

def determine_exp(d):
    if d['sex'] == 'F':
        return random.choice(stat_lst)
    else:
        return False

def make_jackalope():
    jackalope = {'name': make_name(), 'age': '', 'sex': determine_sex(), 'pregnant': False,}
    return jackalope

print(make_jackalope())

jackalope_pop = [make_jackalope(), make_jackalope()]
counter = 0
print(jackalope_pop)
while len(jackalope_pop) < 1000:
    for index in range(len(jackalope_pop)):
        jackalope_pop[index] += 1
    for jackalope in jackalope_pop:
        if jackalope in range(4,9):
            jackalope_pop.append(make_jackalope())
    for i in range(len(jackalope_pop)-1, -1, -1):
        if jackalope_pop[i] == 10:       
            jackalope_pop.pop(i)
    print(jackalope_pop) 
    counter += 1
    print(f"~~~ Counter: {counter} ~~~")      
   
print(f"~~~ Number of jackalopes: {len(jackalope_pop)} ~~~")            
