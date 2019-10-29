import random

# population of non preg jackalopes
jackalope_population = [
    {'name': 'Greatest Grandpa', 'age': 0, 'sex': 0, 'preg': False},
    {'name': 'Greatest Grandma', 'age': 0, 'sex': 1, 'preg': False}
]
# population of preg jackalops
preg_jack = []

year_counter = 0

# function takes a jack and returns true/false if they are of breeding age
def is_breedable_male(jack):
    return jack['age'] >= 4 and jack['age'] <= 8 and jack['sex'] == 0

# function takes a jack and returns true/false if they are of breeding age
def is_breedable_female(jack):
    return jack['age'] >= 4 and jack['age'] <= 8 and jack['sex'] == 1 and jack['preg'] == False

while len(jackalope_population) <= 1000:
    # print(jackalope_population)

    # add newly born jacks
    # iterate through preg jacks
    for jack in jackalope_population:                                                              
        # if pregnant
        if jack['preg']:
            # add one baby with age 0, random name, random gender (male = 0, female = 1)
            jackalope_population.append( {'name': 'randomizebabyname', 'age': 0, 'sex': random.randint(0,1), 'preg': False} )

    # iterate through the list of non-pregnant jacks
    for i in range(0,len(jackalope_population)):
        # if male and of breeding age
        if is_breedable_male(jackalope_population[i]):
            # look at the jack at n-1 and n+1
            if i != 0 and is_breedable_female(jackalope_population[i-1]):
                    # pop female from non-preg list, append them to preg list
                    jackalope_population[i-1]['preg'] = True
            if i != (len(jackalope_population)-1) and is_breedable_female(jackalope_population[i+1]):
                    # pop female from non-preg list, append them to preg list
                    jackalope_population[i+1]['preg'] = True      


    # iterate through jack population and remove those who are too old
    for i in range(len(jackalope_population)-1, -1, -1):
        if jackalope_population[i]['age'] == 10:
            jackalope_population.pop(i)
            print(f'removing a jack')

    # # make remaining jack one year older
    for jack in jackalope_population:
        jack['age'] += 1    
    
    # shuffle population
    random.shuffle(jackalope_population)

    year_counter += 1
    print(f'end of year. there are now {len(jackalope_population)} jackalopes and it is year counter is {year_counter}')
    # print(jackalope_population)

