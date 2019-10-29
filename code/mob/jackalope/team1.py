

# population of jackalopes
jackalope_population = [0,0]
year_counter = 0

while len(jackalope_population) <= 1000:
    mate_counter = 0
    # print(jackalope_population)
    for i in range(0,len(jackalope_population)):
        print(f' jack is {jackalope_population[i]}')
        if jackalope_population[i] >= 4 and jackalope_population[i] <= 8:
            mate_counter += 1
            # print(f'mate counter is {mate_counter}')
        elif jackalope_population[i] >= 10:
            jackalope_population.pop(jackalope_population[i])
        else:
            pass
        jackalope_population[i] += 1

    for i in range(0,mate_counter//2):
        jackalope_population.append(0)
        jackalope_population.append(0)
        jackalope_population.append(0)
        jackalope_population.append(0)
        # jackalope_population.append(0) ** 4   

    year_counter += 1
    print(f'there are now {len(jackalope_population)} jackalopes and it is year {year_counter}')

