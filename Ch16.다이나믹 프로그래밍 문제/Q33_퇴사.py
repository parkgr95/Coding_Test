# 0809
# 퇴사
# idea: 다이나믹 프로그래밍
import sys

n = int(sys.stdin.readline().rstrip())

t, p = [], []
for _ in range(n):
    a, b = map(int,sys.stdin.readline().split())
    t.append(a)
    p.append(b)

d = [0] * (n+1)
for i in range(n-1, -1, -1):
    if t[i] + i > n:
        d[i] = d[i+1]
    else:
        d[i] = max(d[i+1], p[i] + d[i+t[i]])

print(d[0])