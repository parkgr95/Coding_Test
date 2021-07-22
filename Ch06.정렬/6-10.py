# 0722
# idea: 정렬 라이브러리를 사용해 내림차순 정렬
import sys

n = int(sys.stdin.readline().strip())
arr = [sys.stdin.readline().strip() for _ in range(n)]

arr = sorted(arr, reverse=True)

for i in arr:
    print(i, end=' ')