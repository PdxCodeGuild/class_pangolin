'''
Peaks and valleys lab
written by Rhornberger
last update oct 30 2019
'''
# gather data and give it a place to be
import string
data_point = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
peaks_data = []
valley_data = []
# find the indices for the peaks
for index in range(1, len(data_point) -1):
    if data_point [index -1] < data_point[index] and data_point[index + 1 ] < data_point[index]:
        peaks_data.append(index)
  
#print(peaks_data)
# find the indices for the valleys
for index in range(1, len(data_point) -1):
    if data_point [index -1] > data_point[index] and data_point[index +1] > data_point[index]:
        valley_data.append(index)
#print(valley_data)
#return the data
data = peaks_data + valley_data
data.sort()
print(data)
