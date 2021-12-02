from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque(virus)
    while q:
        v, cnt, x, y = q.popleft()
        if cnt == s:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not B[nx][ny]:
                B[nx][ny] = v
                q.append((v, cnt + 1, nx, ny))

if __name__ == "__main__":
    n, k = map(int, input().split())
    B, virus = [], []
    for i in range(n):
        B.append(list(map(int, input().split())))
        for j in range(n):
            if B[i][j]:
                virus.append((B[i][j], 0, i, j))
    virus.sort()
    s, tx, ty = map(int, input().split())
    bfs()
    print(B[tx-1][ty-1])