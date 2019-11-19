data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

is_peaks = []
is_valley = []


def peaks(data):
    for i in range(0, len(data) - 1):
        if data[i] > data[i - 1] and data[i] > data[i + 1]:
            is_peaks.append(i)
    return is_peaks


print(peaks(data))


def valley(data):
    for i in range(0, len(data) - 1):
        if data[i] < data[i - 1] and data[i] < data[i + 1]:
            is_valley.append(i)
    return is_valley


print(valley(data))


def peaks_and_valleys(data):
    is_peaks = peaks(data)
    is_valley = valley(data)

    peaks_valley = is_peaks + is_valley
    peaks_valley.sort()
    return peaks_valley


print(peaks_and_valleys(data))
