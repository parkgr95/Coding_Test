# 0726
# idea: 노드의 개수가 100개 이하니 플로이드 워셜 알고리즘을 사용하는 게 유리하다. 기존 코드와는 다르게 서로에게 가는 비용이 다 1임을 주의
# 미래 도시
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
    g[j][i] = 1

x, k = map(int, sys.stdin.readline().split())

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            g[i][j] = min(g[i][j], g[i][k] + g[k][j])

ans = g[1][k] + g[k][x]
print(-1) if ans == INF else print(ans)