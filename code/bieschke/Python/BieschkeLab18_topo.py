#BieschkeLab18 peaks and valleys.py 
'''
peaks - Returns the indices of peaks. 
A peak has a lower number on both the left and the right.

valleys - Returns the indices of 'valleys'. 
A valley is a number with a higher number on both the left and the right.

peaks_and_valleys - uses the above two functions to compile a single 
list of the peaks and valleys in order of appearance in the original data.
'''
import random
#data = [1, 2, 3, 2, 1]
#data = [3, 2, 1, 2, 3]
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
#data = []

peak_list = []
valley_list = []
topo_list = []

def dataset(x):
    while len(data) < 25:
        dig = random.randint(1, 9)
        data.append(dig)

def peak():
    for i in range(1, len(data)-1):
        if data[i] > data[i + 1]:
            if (data[i] > data[i - 1]):
                print(f"peak at {i}")
                peak_list.append(i)
        elif data[i] < (data[i + 1]):
            pass
        elif data[i] < (data[i - 1]):
            pass
        else:
            print("Peak - Sayonara!")
            quit()

def valley():
    for i in range(1, len(data)-1):        
        if data[i - 1] > data[i]: 
            if (data[i + 1] > data[i]):
                print(f"valley at {i}")
                valley_list.append(i)
        elif data[i] > (data[i + 1]):
            pass
        elif data[i] > (data[i - 1]):
            pass
        else:
            print("Valley - Sayonara!")
            quit()

def topo():
    topo_list = peak_list + valley_list
    print(topo_list)

#dataset(25)
#print(data)
peak()
valley()
print(peak_list)
print(valley_list)
topo()