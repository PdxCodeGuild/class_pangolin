# Taylor Rebbe
# PDX Code Guild
# Lab_18
# 10/30/2019

mtn_range = [1,	2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

#peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.

#valleys - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.

#peaks_and_valleys - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.

peak_lst = []
valley_lst = []
peaks_and_valleys = []
peaks_and_valleys.append(peak_lst)
peaks_and_valleys.append(valley_lst)

for i in range(len(mtn_range)):

    try:
        if  mtn_range[i - 1]  < mtn_range[i]  > mtn_range[i + 1]:
            peak_lst.append(mtn_range[i])
        if i == 0:
            continue
        if  mtn_range[i - 1] > mtn_range[i] < mtn_range[i + 1]:
            valley_lst.append(mtn_range[i])
    except:
        pass


print("Peak", peak_lst )
print("Valley", valley_lst)
print("\nPeaks and Valleys > ",peaks_and_valleys)

