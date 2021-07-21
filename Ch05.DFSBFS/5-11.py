# 0721
# idea: bfs를 이용해 출구까지 이동한 칸의 개수를 구한다.
from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
# strip(): 문자열 맨 앞과 맨 끝의 공백문자를 제거
arr = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    global ans
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        # 미로의 출구에 도착하면 종료
        if x == n-1 and y == m-1:
            break
        arr[x][y] = 0
        ans += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny]:
                arr[nx][ny] = 0
                q.append((nx, ny))
ans = 0
bfs(0, 0)
# 처음 시작 칸 빼기
print(ans - 1)

# 회고: 모든 갈 수 있는 칸을 방문하는 게 아니기 때문에 도착 장소에서 bfs() 함수를 끝내야 한다.