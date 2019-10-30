# number_to_phrase.py
""""
objectives
1. Create user input for number
2. Parse user input into usable numbers
3. Create lists/dicts to define words to numbers
4. Use parsed numbers to pull from list/dict
5. Polish input statement and prints
6. Clean up
"""
#### 1. Create user input for number
user_num = int(input("Enter a number between 0 and 99: "))

#### 2. Parse user input into usable numbers
tens_digit = user_num//10
ones_digit = user_num%10


#### 3. Create lists/dicts to define words to numbers
## make list instead of dict
# ones_to_word = {1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five', 6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine'}
# tens_to_word = {1 : 'ten', 2 : 'twenty', 3 : 'thirty', 4 : 'fourty', 5 : 'fifty', 6 : 'sixty', 7 : 'seventy', 8 : 'eighty', 9 : 'ninety'}
# special_num_word = {11 : 'eleven', 12 }
ones_list = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'niner']
tens_list = ['ten', 'twenty', 'thirty','fourty','fifty', 'sixty', 'seventy', 'eighty', 'ninety']
teen_list = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

#### 4. Use parsed numbers to pull from list/dict
if user_num == 0:
    print(ones_list[0])
if user_num in range(1,10):
    print(ones_list[user_num])
if user_num in range(10,20):
    print(teen_list[user_num-10])
if user_num in range(20,100):
    print(tens_list[tens_digit-1] + '-' + ones_list[ones_digit])

