#lab_18
#Peaks and Vallies
#Jeff Smith

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
peaks = []
valleys = []


for index in range(1, len(data) - 1):
    if data[index - 1] < data[index] and data[index + 1] < data[index]:
        peaks.append([index])
print(peaks)

for index in range(1, len(data) - 1):
    if data[index - 1] > data[index] and data[index + 1] > data[index]:
        valleys.append([index])
print(valleys)

pandv = peaks + valleys
pandv.sort()
print(pandv)