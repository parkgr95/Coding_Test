"""
22-03-21
idea : 계수 정렬
"""
arr = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

cnt = [0] * (max(arr) + 1)

for a in arr:
    cnt[a] += 1

for i in range(len(cnt)):
    for j in range(cnt[i]):
        print(i, end=' ')