# 0727
# 도시 분할 계획
# idea : 크루스칼 알고리즘을 이용하여 최소 신장 트리를 찾은 뒤 가장 큰 간선, 즉 마지막 값을 빼줘 최적의 해를 구해준다.
import sys

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range(m+1)]

edges = []
for _ in range(n):
    a, b, cost = map(int, sys.stdin.readline().split())
    edges.append((cost, a, b))

edges.sort()

ans = 0
last = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        ans += cost
        last = cost

print(ans - last)