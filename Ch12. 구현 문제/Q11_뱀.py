# 0730
# 뱀
# idea: 전형적인 시뮬레이션 문제다. 조건에 따라 코드를 만든다.
import sys

n = int(sys.stdin.readline().strip())
arr = [[0] * (n + 1) for _ in range(n + 1)]

k = int(sys.stdin.readline().strip())
for _ in range(k):
    a, b = map(int, sys.stdin.readline().split())
    arr[a][b] = 1

l = int(sys.stdin.readline().strip())
info = []
for _ in range(l):
    x, c = sys.stdin.readline().split()
    info.append((int(x), c))

# 방향: 동, 남, 서, 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def turn(direction, c):
    if c == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction


x, y = 1, 1
arr[x][y] = 2
direction = 0
time = 0
idx = 0
# 뱀 정보
q = [(x, y)]
while True:
    nx = x + dx[direction]
    ny = y + dy[direction]
    if 1 <= nx <= n and 1 <= ny <= n and arr[nx][ny] != 2:
        # 사과가 없으면
        if arr[x][y] == 0:
            arr[nx][ny] = 2
            q.append((nx, ny))
            # 꼬리
            px, py = q.pop(0)
            arr[px][py] = 0
        # 사과가 있으면
        if arr[x][y] == 1:
            arr[nx][ny] = 2
            q.append((nx, ny))
    else:
        time += 1
        break
    x, y = nx, ny
    time += 1
    # 방향 변환 정보 시간일 때
    if idx < l and time == info[idx][0]:
        direction = turn(direction, info[idx][1])
        idx += 1

print(time)
