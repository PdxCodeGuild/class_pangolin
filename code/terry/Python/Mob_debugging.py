# population of jackalopes
jackalope_population = [0, 0]
year_counter = 0

while len(jackalope_population) <= 1000:

    # counter for tracking number of eligible singles
    mate_counter = 0

    # iterate through jack population and figure out how many of breeding age
    for jack in jackalope_population:
        # if jack is of breeding age
        if jack >= 4 and jack <= 8:
            # increment jack counter
            mate_counter += 1

    # iterate through jack population and remove those who are too old
    # count how many old jacks
    old_jack_count = jackalope_population.count(10)
    print(f'removing {old_jack_count} jacks')

    # remove that many jacks
    for i in range(0, old_jack_count):
        jackalope_population.remove(10)

    # add newly born jacks
    print(f'adding {(mate_counter // 2) * 2} new babies')
    for i in range(0, mate_counter // 2):
        jackalope_population.append(0)
        jackalope_population.append(0)

    # make remaining jack one year older
    jackalope_population = [jack + 1 for jack in jackalope_population]

    year_counter += 1
    print(f'end of year. there are now {len(jackalope_population)} jackalopes and it is year counter is {year_counter}')
    # print(jackalope_population)
