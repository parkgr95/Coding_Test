# 0809
# 병사 배치하기
# idea: 가장 긴 증가하는 부분 수열(LIS)
import sys

n = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().split()))
data.reverse()

d = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if data[j] < data[i]:
            d[i] = max(d[i], d[j]+1)

print(n-max(d))