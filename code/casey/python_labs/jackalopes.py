jackalope_pop = [0, 0]
counter = 0
print(jackalope_pop)
while len(jackalope_pop) < 1000:
    for index in range(len(jackalope_pop)):
        jackalope_pop[index] += 1
    for jackalope in jackalope_pop:
        if jackalope in range(4,9):
            jackalope_pop.append(0)
    for i in range(len(jackalope_pop)-1, -1, -1):
        if jackalope_pop[i] == 10:       
            jackalope_pop.pop(i)
    print(jackalope_pop) 
    counter += 1
    print(f"~~~ Counter: {counter} ~~~")      
   
print(f"~~~ Number of jackalopes: {len(jackalope_pop)} ~~~")
 
            
        

     # for jackalope in jackalope_pop:
    #     if jackalope > 9:       
    #         jackalope_pop = jackalope_pop.remove(jackalope)
        
   
            
           
         