'''
Average numbers lab 01
written by Rhornberger
last updated oct 23 2019
'''
nums = [5, 0, 8, 3, 4, 1, 6]
print('The number of intergers in the list is', len(nums))
print()

tot = 0
for i in nums:
    tot = tot + i
print(f'The total of the list is {tot}')
print()
tot = tot / 7 
tot = round(tot, 3)
print(f'The average number for all the numbers in the list is {tot}')


