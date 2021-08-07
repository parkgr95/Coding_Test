# 0804
# 연구소
# idea: bfs, 완전 탐색
import copy
import sys
from collections import deque

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 바이러스가 퍼진 뒤 안전 영억 크기를 구해준다.
def bfs():
    global ans
    q = deque()
    s = copy.deepcopy(graph)
    for i in range(n):
        for j in range(m):
            if s[i][j] == 2:
                q.append((i, j))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and s[nx][ny] == 0:
                s[nx][ny] = 2
                q.append((nx, ny))
    result = 0
    for x in s:
        result += x.count(0)
    ans = max(ans, result)

# 벽을 세우는 함수
def wall(cnt):
    # 벽을 3개 세운 뒤, 바이러스를 퍼드린다.
    if cnt == 3:
        bfs()
        return
    # 빈 공간에 울타리 설치
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                wall(cnt+1)
                graph[i][j] = 0

if __name__ == "__main__":

    n, m = map(int, sys.stdin.readline().split())
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    ans = 0
    wall(0)
    print(ans)
