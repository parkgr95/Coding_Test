from collections import deque


def bfs():
    q = deque([x])
    while q:
        now = q.popleft()
        for next in graph[now]:
            if distance[next] == -1:
                distance[next] = distance[now] + 1
                q.append(next)


if __name__ == "__main__":
    n, m, k, x = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)

    distance = [-1] * (n + 1)
    distance[x] = 0

    bfs()

    check = False
    for i, d in enumerate(distance):
        if d == k:
            print(i)
            check = True

    if not check:
        print(-1)