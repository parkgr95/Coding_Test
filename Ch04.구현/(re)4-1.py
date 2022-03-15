"""
12-03-15
idea : 이동 계획에 따라 좌표 이동
"""
n = int(input())
arr = list(map(str, input().split()))

dic = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
x, y = 1, 1

for a in arr:
    dx, dy = dic[a]
    nx, ny = x + dx, y + dy
    if nx <= 0 or nx > n or ny <= 0 or ny > n:
        continue
    x, y = nx, ny

print(x, y)