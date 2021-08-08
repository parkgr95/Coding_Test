# 0808
# 감시 피하기
# idea: bfs, 완전 탐색
import copy
import sys
from collections import deque
from itertools import combinations

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque(teacher)
    s = copy.deepcopy(graph)
    while q:
        x, y = q.popleft()
        # 각 방향마다 학생이 있는 지 확인
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

    n = int(sys.stdin.readline().rstrip())
    graph, teacher, space = [], [], []
    for i in range(n):
        graph.append(list(map(str, sys.stdin.readline().split())))
        for j in range(n):
            if graph[i][j] == 'T':
                teacher.append((i, j))
            elif graph[i][j] == 'X':
                space.append((i, j))

    check = False
    for data in combinations(space, 3):
        for x, y, in data:
            graph[x][y] = 'O'
        if bfs():
            check = True
            break
        for x, y, in data:
            graph[x][y] = 'X'

    print('YES') if check else print('NO')

# 회고: 완전히 bfs가 아닌 각 방향마다 확인을 해주는 문제이므로, 방향을 먼저 정하고 bfs를 진행할 것!