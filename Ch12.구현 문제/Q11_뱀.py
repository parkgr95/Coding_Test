# 0730
# 뱀
# idea: 전형적인 시뮬레이션 문제다. 조건에 따라 코드를 만든다.
import sys
from collections import deque

# 방향: 동, 남, 서, 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    x, y = 1, 1 # 뱀의 초기 위치
    arr[x][y] = 2 # 뱀이 있는 곳은 2로 표시
    direction = 0 # 초기 방향
    time = 1
    q = deque([(x, y)]) # 뱀 정보
    while True:
        x, y = x + dx[direction], y + dy[direction]
        if 1 <= x <= n and 1 <= y <= n and arr[x][y] != 2:
            # 사과가 없으면 꼬리 제거
            if not arr[x][y] == 1:
                px, py = q.popleft()
                arr[px][py] = 0
            arr[x][y] = 2
            q.append([x, y])
            if time in info:
                direction = turn(direction, info[time])
            time += 1
        else:
            return time

if __name__ == "__main__":

    n = int(sys.stdin.readline().strip())

    # 맵 정보(사과가 있는 곳은 1)
    arr = [[0] * (n + 1) for _ in range(n + 1)]
    for _ in range(int(sys.stdin.readline().strip())):
        a, b = map(int, sys.stdin.readline().split())
        arr[a][b] = 1

    # 방향 회전 정보
    info = {}
    for _ in range(int(sys.stdin.readline().strip())):
        x, c = sys.stdin.readline().split()
        info[int(x)] = c
    print(simulate())