"""
22-03-21
idea : 정렬 라이브러리 사용
"""
arr = [int(input()) for _ in range(int(input()))]

arr.sort(reverse=True)

for a in arr:
    print(a, end=' ')
