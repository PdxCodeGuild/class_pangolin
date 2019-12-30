# lab_15b.py
# Jeff Smith
# Lab 15: Number to Phrase

ones = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
        5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
twos = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
        15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
tens = {0: '', 1: '', 2: 'twenty', 3: 'thirty', 4: 'forty',
        5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}
huns = {0: '', 1: 'one hundred', 2: 'two hundred', 3: 'three hundred', 4: 'four hundred',
        5: 'five hundred', 6: 'six hundred', 7: 'seven hundred', 8: 'eight hundred', 9: 'nine hundred'}

num = int(input('Enter a number 0-999: '))


def textnum(num):
    if num == 0:
        return 'zero'
    elif num > 0 and num <= 9:
        return ones[num]
    elif num >= 10 and num <= 19:
        return twos[num]
    elif num >= 20 and num <= 99:
        n1 = num // 10
        n2 = num % 10
        return tens[n1] + '-' + ones[n2]
    elif num >= 100 and num < 1000:
        n1 = num % 1000 // 100
        n2 = num % 100 // 10
        n3 = num % 10
        print(n1, n2, n3)
        return ones[n3] + 'hundred, ' + tens[n1] + '-' + ones[n2]
        return huns[n3] + tens[n1] + '-' + ones[n2]

    else:
        print("Number out of range")


print(textnum(num))
