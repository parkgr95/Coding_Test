from collections import deque
import copy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    global ans
    q = deque()
    s = copy.deepcopy(B)
    for i in range(n):
        for j in range(m):
            if s[i][j] == 2:
                q.append((i, j))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not s[nx][ny]:
                s[nx][ny] = 2
                q.append((nx, ny))
    result = 0
    for x in s:
        result += x.count(0)
    ans = max(ans, result)

def wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if B[i][j] == 0:
                B[i][j] = 1
                wall(cnt+1)
                B[i][j] = 0

if __name__ == "__main__":
    n, m = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    wall(0)
    print(ans)