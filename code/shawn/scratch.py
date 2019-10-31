
data = [1,2,3,4,5,6,5,4,3,2,1]

width = len(data)
height = 7



for y in range(height,0,-1):
    for x in range(width):
        if data[x] < y:
            print('  ', end='')
        elif data[x] >= y:
            print('X ', end='')
    print()

