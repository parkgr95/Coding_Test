from itertools import combinations
from collections import deque
import copy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque(teacher)
    s = copy.deepcopy(B)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x, y
            while 0 <= nx < n and 0 <= ny < n:
                if s[nx][ny] == 'S':
                    return False
                elif s[nx][ny] == 'O':
                    break
                nx, ny = nx + dx[i], ny + dy[i]
    return True

if __name__ == "__main__":
    n = int(input())
    B, teacher, space = [], [], []
    for i in range(n):
        B.append(list(map(str, input().split())))
        for j in range(n):
            if B[i][j] == 'T':
                teacher.append((i, j))
            elif B[i][j] == 'X':
                space.append((i, j))

    check = False
    for block in combinations(space, 3):
        for x, y, in block:
            B[x][y] = 'O'
        if bfs():
            check = True
            break
        for x, y, in block:
            B[x][y] = 'X'

    print('YES' if check else 'NO')