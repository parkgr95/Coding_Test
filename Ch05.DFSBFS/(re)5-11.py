"""
22-03-15
idea : bfs를 수행하여 모든 노드의 값을 거리 정보로 넣기
"""
from collections import deque

n, m = map(int, input().split())
B = [list(map(int, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False] * m for _ in range(n)]

def bfs(i, j):
    q = deque()
    q.append((i, j))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and B[x][y] and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
                B[nx][ny] = B[x][y] + 1
    return B[n-1][m-1]

print(bfs(0, 0))