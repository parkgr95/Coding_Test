# 0804
# 특정 거리의 도시 찾기
# idea: bfs
import sys
from collections import deque

def bfs():
    q = deque([x])
    while q:
        now = q.popleft()
        for next in graph[now]:
            if distance[next] == -1:
                distance[next] = distance[now] + 1
                q.append(next)
    return

if __name__ == "__main__":

    n, m, k, x = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)

    distance = [-1] * (n+1)
    distance[x] = 0

    bfs()

    check = False
    for i in range(1, n + 1):
        if distance[i] == k:
            print(i)
            check = True

    if check == False:
        print(-1)