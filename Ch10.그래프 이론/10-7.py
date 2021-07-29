# 0727
# 팀 결성
# idea: 개선된 서로소 집합 알고리즘을 사용하여 조건에 따라 집합을 합치거나, 같은 집합에 속해있는 지 판단해준다,
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

parent = [i for i in range(0, n+1)]

for i in range(m):
    op, a, b = map(int, sys.stdin.readline().split())
    if op == 0:
        union_parent(parent, a, b)
    else:
        print('yes') if find_parent(parent, a) == find_parent(parent, b) else print('no')