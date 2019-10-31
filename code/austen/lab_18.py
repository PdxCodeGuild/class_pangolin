

#test data 
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

#peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.

def peaks(data):

    peaks_list = []
#starting at 1 and stepping -1 makes it so we dont check the beginging or the end because it does not matter 
    for i in range(1,len(data)-1):
        if data[i] > data[i-1] and data[i] > data[i+1]:
            peaks_list.append(i)
    return peaks_list
    
print(peaks(data))

#alleys - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.

def valley(data):

    valley_list = []
#starting at 1 and stepping -1 makes it so we dont check the beginging or the end because it does not matter
    for i in range(1,len(data)-1):
        if data[i] < data[i-1] and data[i] < data[i+1]:
            valley_list.append(i)
    return valley_list
print(valley(data))

#peaks_and_valleys - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.

def peaks_and_vallys(data):

    peaks_list = peaks(data)
    valley_list = valley(data)

    peaks_valley = peaks_list + valley_list
    peaks_valley.sort()
    return peaks_valley
print (peaks_and_vallys(data))