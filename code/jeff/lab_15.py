#lab_15.py
#Jeff Smith
#Lab 15: Number to Phrase

# Convert a given number into its english representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.
# Hint 2: use the digit as an index for a list of strings OR as a key for a dict of digit:phrase pairs.

ones = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
twos = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
tens = {0: '', 1: '', 2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}

def textnum(num):
    if num == 0:
        return 'zero'
    elif num > 0 and num <= 9:
        return ones[num]
    elif num >= 10 and num <= 19:
        return twos[num]
    elif num >=20 and num <= 99:
        n1 = num // 10
        n2 = num % 10
        return tens[n1] + '-' + ones[n2]
    else:
        print("Number out of range")

num = int(input('Enter a number 0-100: '))
print(textnum(num))
