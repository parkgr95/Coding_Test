"""
22-03-21
idea : 퀵 정렬
"""
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pvt = arr[0]
    tail = arr[1:]

    left = [x for x in tail if x <= pvt]
    right = [x for x in tail if x > pvt]

    return quick_sort(left) + [pvt] + quick_sort(right)

print(quick_sort(arr))