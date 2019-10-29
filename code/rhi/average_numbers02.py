'''
Average numbers lab 02
written by Rhornberger
last update oct 23 2019
'''
user_choice = input('please enter a number or enter done when you are finished: ').lower()
user_list = []
while user_choice != 'done':
    user_list.append(user_choice)
    user_choice = input('please enter a number or enter done when you are finished: ').lower()
print(user_list)
print(f'{len(user_list)} is number of numbers in your list')
user_list = [int(i) for i in user_list]
tot = 0   
for i in user_list:
    tot = tot + i
print(f'{tot} is the total of the numbers you entered')
tot = tot / len(user_list)
tot = round(tot, 3)
print(f'{tot} is the average of the numbers you entered!')
print('Thank you.')

