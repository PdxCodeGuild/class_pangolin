card_num = input("What is your card number?")
old_list = list(card_num)
new_list = [int(num) for num in old_list]
last = (new_list.pop())
new_list.reverse()

#double every other
def double_other():
    for i in range(0, len(new_list), 2):
        new_list[i] *= 2
    return new_list
double_other()

# -9 if num > 9
new_list2 = [num - 9 if num > 9 else num for num in new_list]
# sum of list
total = sum(new_list2)
total_str = str(total)
second_num = int(total_str[1])


if second_num == last:
    print("Your card is verified.")
else:
    print("Card not valid.")
