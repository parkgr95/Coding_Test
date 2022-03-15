"""
22-03-15
idea : dfs를 사용해 연결되어 있는 노드 묶음을 세준다
"""
n, m = map(int, input().split())
B = [list(map(int, input())) for _ in range(n)]

ans = 0

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if not B[x][y]:
        B[x][y] = 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False

for x in range(n):
    for y in range(m):
        if dfs(x, y):
            ans += 1

print(ans)
