# lab_09.py , versions 1-4
# # Jeff Smith

import math

d = int(input('Welcome. What is the distance? '))
unit = input(
    'What are the units you want to convert from? (i -for inches, f -for feet, y -for yards, m -for miles, k -for kilometer, or me -for meters): ').lower()


def d2m(d, unit):
    i = .0254
    f = 0.3048
    y = 0.9144
    m = 1609.34
    me = 1
    k = 1000

    meters = []
    if unit == 'me':
        meters.append(d * me)
    elif unit == 'i':
        meters.append(d * i)
    elif unit == 'f':
        meters.append(d * f)
    elif unit == 'y':
        meters.append(d * y)
    elif unit == 'm':
        meters.append(d * m)
    elif unit == 'k':
        meters.append(d * k)
    else:
        print('Please choose "in -for inches, ft -for feet, yd -for yards, mi -for miles, km -for kilometer, or me -for meters: ')
    # print(meters)
    return meters


d2m(d, unit)


def con(meters, d, unit):
    print(meters[0])
    output = input(
        'What are the units you want to convert to? (i -for inches, f -for feet, y -for yards, m -for miles, k -for kilometer, or me -for meters): ').lower()
    final = []
    while len(final) < 1:
        if output == 'me':
            final.append(meters[0] / 1)
        elif output == 'i':
            final.append(meters[0] / 0.0254)
        elif output == 'f':
            final.append(meters[0] / 0.3048)
        elif output == 'y':
            final.append(meters[0] / 0.9144)
        elif output == 'm':
            final.append(meters[0] / 1609.34)
        elif output == 'k':
            final.append(meters[0] / 1000)
        else:
            print('Please choose "i -for inches, f -for feet, y -for yards, m -for miles, k -for kilometer, or me -for meters: ')
            continue
    print(f'{d} {unit} is {final[0]} {output}')


con(d2m(d, unit), d, unit)
# print(f'{d} {unit} is {final} {output}')
