from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    global check
    q = deque([(i, j)])
    temp = [(i, j)]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visted[nx][ny] and l <= abs(B[nx][ny] - B[x][y]) <= r:
                visted[nx][ny] = True
                q.append((nx, ny))
                temp.append((nx, ny))
    if len(temp) > 1:
        check = True
        num = sum([B[x][y] for x, y in temp]) // 4
        for x, y in temp:
            B[x][y] = num

if __name__ == "__main__":
    n, l, r = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    while True:
        visted = [[False] * n for _ in range(n)]
        check = False
        for i in range(n):
            for j in range(n):
                if not visted[i][j]:
                    visted[i][j] = True
                    bfs(i, j)
        if not check:
            break
        ans += 1
    print(ans)