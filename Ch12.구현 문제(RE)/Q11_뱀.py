from collections import deque

# 우, 하, 좌, 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(d, c):
    if c == 'L':
        d = (d - 1) % 4
    else:
        d = (d + 1) % 4
    return d

def game(x, y):
    cnt = 1  # 시간
    d = 0  # 방향
    q = deque([(x, y)])
    while True:
        x, y = x + dx[d], y + dy[d]
        if 0 <= x < n and 0 <= y < n and B[x][y] != 2:
            if not B[x][y] == 1:
                tx, ty = q.popleft()
                B[tx][ty] = 0
            B[x][y] = 2
            q.append((x, y))
            if cnt in dir:
                d = turn(d, dir[cnt])
            cnt += 1
        else:
            return cnt

if __name__ == "__main__":
    n = int(input())
    B = [[0] * n for _ in range(n)]
    B[0][0] = 2
    for _ in range(int(input())):
        i, j = map(int, input().split())
        B[i-1][j-1] = 1
    dir = {}
    for _ in range(int(input())):
        x, c = input().split()
        dir[int(x)] = c
    print(game(0, 0))