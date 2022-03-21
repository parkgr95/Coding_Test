"""
22-03-21
idea : 선택 정렬
"""
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_ = i
    for j in range(i+1, len(array)):
        if array[min_] > array[j]:
            min_ = j
    array[i], array[min_] = array[min_], array[i]

print(array)