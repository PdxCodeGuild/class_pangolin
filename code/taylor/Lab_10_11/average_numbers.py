# Taylor Rebbe
# PDX Coed Guild
# Lab_10v1

message1 = "\nenter a number, or "
message2 = "enter a number, or 'done': >"
message4 = "\nTo exit type done: >"

nums = [5, 0, 8, 3, 4, 1, 6]

sums = 0

game_over = ""


while game_over != "done":
    for i in range(len(nums)):
        sums += nums[i]
        average = sums / len(nums)

    print(sums)
    print(average)


  

    game_over = input(message4)
    sums = 0
    print("\nBye bye")


    nums = []
nums.append(5)
print(nums)

