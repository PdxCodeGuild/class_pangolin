

# population of jackalopes
jackalope_population = [0,0]
year_counter = 0

while len(jackalope_population) <= 1000:
    mate_counter = 0
    # print(jackalope_population)
    for i in range(0, len(jackalope_population)):
        print(f' jack is {(i)}')
        if jackalope_population[i] >= 4 and jackalope_population[i] <= 8:
            mate_counter += 1
            # print(f'mate counter is {mate_counter}')
            jackalope_population[i] += 1
        
        else:
            jackalope_population[i] += 1

    temp_list = []
    for jack in jackalope_population:
        if jack <= 10:
            temp_list.append(jack)

    jackalope_population = temp_list.copy()    
        
        #print([i])

    for i in range(0,mate_counter//2):
        jackalope_population.append(0)
        jackalope_population.append(0)
        jackalope_population.append(0)
        jackalope_population.append(0)
        # jackalope_population.append(0) ** 4   

    year_counter += 1
    print(f'there are now {len(jackalope_population)} jackalopes and it is year {year_counter}')

