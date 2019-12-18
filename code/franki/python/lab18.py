data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
def peaks(x):
    peaks_result = []
    for i in range(1, len(x)-1, 1):
        if x[i - 1] < x[i]: 
            if x[i + 1] < x[i]:  
                peaks_result.append(i)
    return peaks_result
        
def valleys(x):
    valleys_result = []
    for i in range(1, len(x)-1, 1):
        if x[i-1] > x[i]: 
            if x[i] < x[i+1]: 
                valleys_result.append(i)
    return valleys_result


print(peaks(data))
print(valleys(data))
        