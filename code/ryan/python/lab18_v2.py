data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
def draw_x():
    drawing = ""
    for num in data:
        print("X"\n) * num

def peaks():
    peaks = []
    for i in range(1, len(data)-1):
        if data[i] > data[i-1] and data[i] > data[i+1]:
            peaks.append(i)
    return peaks

def valleys():
    valleys = []
    for i in range(1, len(data)-1):
        if data[i] < data[i-1] and data[i] < data[i+1]:
            valleys.append(i)
    return valleys

def peaks_and_valleys():
    compiled = peaks() + valleys()
    compiled.sort()
    return compiled


print(peaks())
print(valleys())
print(peaks_and_valleys())
