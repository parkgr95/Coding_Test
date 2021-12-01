# 0721
# idea: 시뮬레이션, 방향을 설정해주는 것이 핵심. 2차원 리스트를 선언할 때는 컴프리헨션을 이용하는 것이 효율적이다.
# BFS
from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
x, y, d = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

# 상, 하, 좌, 우
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    global ans
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        visited[x][y] = True
        ans += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))

ans = 0
bfs(x, y)
print(ans)

# DFS
import sys

n, m = map(int, sys.stdin.readline().split())
x, y, d = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

def dfs(x, y):
    global ans
    if 0 <= x < n and 0 <= y < m and arr[x][y] == 0 and not visited[x][y]:
        visited[x][y] = True
        ans += 1
        # 상, 하, 좌, 우
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)

ans = 0
dfs(x, y)
print(ans)

# 구현
import sys
n, m = map(int, sys.stdin.readline().split())
x, y, d = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

ans = 1
turn_time = 0
visited[x][y] = True
while True:
    turn_left()
    nx = x + dx[d]
    ny = y + dy[d]
    # 회전한 이후 정면에 육지고 가보지 않은 경우
    if arr[nx][ny] == 0 and not visited[nx][ny]:
        visited[nx][ny] = True
        x, y = nx, ny
        turn_time = 0
        ans += 1
    # 회전한 이후 정면에 바다거나 가 본 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        if arr[nx][ny] == 0:
            x, y = nx, ny
        else:
            break
        turn_time = 0

print(ans)

# 회고: BFS/DFS/구현 순으로 만들어보았다. DFS가 가장 간결하지만 BFS가 가장 빠르지만 주어진 방향을 쓰지 않으므로 구현을 쓰는 게 좋을 것 같다.