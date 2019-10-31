'''
Lab 18: Peaks and Valleys - Version 2

Purpose/goal: Using the data list above, draw the image of X's below

'''
# define data list
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
print(data)

# create peaks function: Returns the indices of peaks. A peak has a lower number on both the left and the right.
def peaks(data):
   peaks_list = []
   for i in range(len(data)):
      try:
         if data[i] > data[i + 1] and data[i] > data[i - 1]:
            peaks_list.append(data[i])
      except: 
         pass
   return peaks_list     

# create valleys function: Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.
def valleys(data):
   val_list = []
   for i in range(len(data)):
      try:
         if data[i] < data[i + 1] and data[i] < data[i - 1]:
            val_list.append(data[i])
      except: 
         pass
   val_list.remove(val_list[0])
   return val_list

# peaks_and_valleys function: uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.
def peaks_and_valleys(data):
   peaks_list = peaks(data)
   val_list = valleys(data)
   p_v = peaks_list + val_list
   return p_v

def draw():
    global data
    width = len(data)
    height = 10
    for y in range(height,0,-1):
        for x in range(width):
            if data[x] < y:
                print("  ", end="")
            elif data[x] >= y:
                print("X ", end="")
        print()        

draw()
print(data)
print(peaks_and_valleys(data))