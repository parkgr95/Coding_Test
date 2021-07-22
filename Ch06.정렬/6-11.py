# 0722
# idea: 정렬 라이브러리와 람다를 사용해 내림차순 정렬
import sys

n = int(sys.stdin.readline().strip())
arr = [list(map(str, sys.stdin.readline().split())) for _ in range(n)]

arr = sorted(arr, key=lambda x: x[1])
for i in arr:
    print(i[0], end=' ')