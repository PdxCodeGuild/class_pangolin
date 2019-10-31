"""
peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.
valleys - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.
peaks_and_valleys - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.
"""

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

is_peak = 0
is_valley = 0

for x, y in zip(data, data[1:]):
    is_peak = 0
    is_valley = 0
    print(x, y)
    if x > y:
        is_peak += x
    elif x < y:
        is_valley += x

print(is_peak)
print(is_valley)
