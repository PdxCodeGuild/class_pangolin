# Peaks and valleys lab18 version 1 10/30/2019 by Wiley Rummel

#Define the following Functions:
#1. peaks() - returns the incices of peaks.  A peak has a lower number on both the left and the right.
#2. valleys()-returns the indices of valleys.  A valley is a number with a higher number on both left and right.
#3. peaks_and_valleys() - uses the above two functions to compile a single list of the peaks and valleys 
#in order of appearance in the original data. 

#input data for stable testing purposes is:
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(x):
    '''returns the indices of peaks.  A peak has a lower number on both the left and right.'''
    peak_list = []
    for i in range(len(x)):
        if i-1 !=0 and x[i-1] < x[i]:
            if i + 1 < len(x) and x[i + 1] < x[i]:
                #print(f"the value is {x[i]}  and {i} is the index")
                peak_list.append(i)
                #print(peak_list)
    return peak_list 

def valleys(x):
    '''returns the indices of valleys. A valley has a lower number on both the left and right.'''
    valley_list = []
    for i in range(len(x)):
        if i !=0 and x[i-1] > x[i]:
            if i + 1 < len(x) and x[i + 1] > x[i]:
                #print(f"the value is {x[i]}  and {i} is the index")
                valley_list.append(i)
                #print(valley_list)
    return valley_list

print(peaks(data))
print(valleys(data))

def peaks_and_valleys():
    peaks_and_valleys_list=[]
    #valleys(data)    
    #peaks(data)
    
    peaks_and_valleys_list = peaks(data) + valleys(data)
    peaks_and_valleys_list.sort()
    return peaks_and_valleys_list
print(peaks_and_valleys())
