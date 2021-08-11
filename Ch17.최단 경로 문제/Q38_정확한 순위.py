# 0811
# 정확한 순위
# idea: 플로이드 워셜 알고리즘
import sys

INF = int(1e9)

n, m = map(int, sys.stdin.readline().split())
g = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            g[i][j] = 0

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    g[i][j] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            g[i][j] = min(g[i][j], g[i][k] + g[k][j])

ans = 0
for i in range(1, n+1):
    cnt = 0
    for j in range(1, n+1):
        if g[i][j] != INF or g[j][i] != INF:
            print(i, j)
            cnt += 1
    if cnt == n:
        ans += 1
print(ans)