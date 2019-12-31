'''
Lab 10: Average Numbers - Version 2

Purpose/goal: Find the average of a user's numbers.

    - Ask the user to enter the numbers one at a time, putting them into a list. - D
    
    - If the user enters 'done', then calculate and display the average - D
    
'''

# define user num list
nums = []

# user greeting
print("Greetings!\nThis is a number averaging program.\n")

# program while loop
go_again = input("Do you have some numbers you'd like to average? (y/n): ").lower()
while go_again == "y":
    print("\nPerfect! Go ahead and give me your numbers!\n")
    if go_again == "n":
        break

    # num input 
    user_input = input("Enter a number or say 'Done': ").lower()
    num = int(user_input)
    # append nums
    nums.append(num)

    # start of input while loop
    while num > 0:
        user_input = input("Enter a number or say 'Done': ").lower()
        if user_input == "done":
            break 
        num = int(user_input)
        nums.append(num)

    # find sum of nums
    run_sum = sum(nums)

    # find average 
    user_av = run_sum / len(nums)

    # tell user the average of their numbers
    print(f"Wonderful! The average of your numbers is: {user_av}\n")

    go_again = input("Would you like to find the average of another set of numbers? (y/n): ")


# program end
print("\nThank you for using this number averaging program.\nGoodbye!")

