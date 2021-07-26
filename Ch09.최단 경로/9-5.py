# 0726
# idea: n과 m의 범위가 충분히 크기 때문에, 우선순위 큐를 이용해서 다익스트라 알고리즘을 작성하는 것이 유리하다.
# 전보
import heapq
import sys

INF = int(1e9)

n, m, c = map(int, sys.stdin.readline().split())
g = [[] for _ in range(n+1)]
d = [INF] * (n+1)

for _ in range(m):
    x, y, z = map(int, sys.stdin.readline().split())
    g[x].append((y, z))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    d[start] = 0
    while q:
        dist, now = heapq.heappush(q)
        if d[now] < dist:
            continue
        for i in g[now]:
            cost = dist + i[1]
            if cost < d[i[0]]:
                d[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(c)
# 도시의 총 개수, 총 걸리는 시간
cnt, tm = 0, 0
for i in d:
    if i != INF:
        cnt += 1
        tm += max(max, i)

# 시작은 제외
print(cnt - 1, tm)

# 회고: 쓰면서 버벅댔다... 다익스트라 알고리즘을 아직 다 익히지 못한 탓이다... 근 시일내로 다시 한 번 봐야할 듯.