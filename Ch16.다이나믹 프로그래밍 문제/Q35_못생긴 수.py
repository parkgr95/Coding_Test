# 0809
# 못생긴 수
# idea: 다이나믹 프로그래밍
import sys

n = int(sys.stdin.readline().rstrip())

d = [0] * n
d[0] = 1

x2 = x3 = x5 = 0 # 2배, 3배, 5배를 위한 인덱스
next2, next3, next5 = 2, 3, 5 # 처음에 곱셈값을 초기화
for i in range(1, n):
    d[i] = min(next2, next3, next5)
    print(next2, next3, next5)
    if d[i] == next2:
        x2 += 1
        next2 = d[x2] * 2
    if d[i] == next3:
        x3 += 1
        next3 = d[x3] * 3
    if d[i] == next5:
        x5 += 1
        next5 = d[x5] * 5

print(d[n-1])