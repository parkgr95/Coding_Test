# 0804
# 경쟁적 전염
# idea: bfs
import sys
from collections import deque

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(data):
    q = deque(data)
    while q:
        virus, s, x, y = q.popleft()
        if s == target_s:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s+1, nx, ny))

if __name__ == "__main__":

    n, k = map(int, sys.stdin.readline().split())

    graph, data = [], []
    for i in range(n):
        graph.append(list(map(int, sys.stdin.readline().split())))
        for j in range(n):
            if graph[i][j] != 0:
                data.append((graph[i][j], 0, i, j))
    data.sort()

    target_s, target_x, target_y = map(int, sys.stdin.readline().split())

    bfs(data)
    print(graph[target_x-1][target_y-1])