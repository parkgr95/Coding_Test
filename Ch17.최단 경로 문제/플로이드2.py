# 0811
# 플로이드 2
# idea: 플로이드 워셜 알고리즘 사용, 여러 노선 중 비용이 작은 값만 사용. 최소 경로도 구하기
import sys

INF = int(1e9) # 무한을 의미하는 값. 10억

# 노드의 개수 및 간선의 개수를 입력받기
n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]
# 각각의 path[a]마다 path[a][b]의 경로를 담은 리스트가 총 n개
path = [[[INF]] * (n+1) for _ in range(n+1)]

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
  # A에서 B로 가는 비용은 C라고 설정
  a, b, c = map(int, sys.stdin.readline().split())
  # 가장 짧은 간선 정보만 저장
  if c < graph[a][b]:
    graph[a][b] = c
    path[a][b] = [a, b]

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      if a != b and graph[a][b] > graph[a][k] + graph[k][b]:
        graph[a][b] = graph[a][k] + graph[k][b]
        # graph[a][b]를 갱신해줄 때마다 path도 갱신해주기
        path[a][b] = path[a][k][:-1] + path[k][b]

# 수행된 결과를 출력
for a in range(1, n + 1):
  for b in range(1, n + 1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력. 도달할 수 있는 경우 거리를 출력
    print(0, end=" ") if graph[a][b] == INF else print(graph[a][b], end=" ")
  print()

for a in range(1, n + 1):
  for b in range(1, n + 1):
    if graph[a][b] == INF or a == b:
      print(0)
    else:
      print(len(path[a][b]), *path[a][b])