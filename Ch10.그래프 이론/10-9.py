# 0727
# 커리큘럼
# idea: 위상절렬을 이용하여 모든 강의를 수강하기 위한 최소 시간을 구한다.
import copy
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
time = [0] * (n+1)

for i in range(1, m+1):
    arr = list(map(int, sys.stdin.readline().split()))
    time[i] = arr[0]
    for x in arr[1:-1]:
        indegree[i] += 1
        graph[x].append(i)

def topology_sort():
    ans = copy.deepcopy(time)
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        ans.append(now)
        for i in graph[now]:
            ans[i] = max(ans[i], ans[now] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in ans:
        print(ans[i])

topology_sort()

# 회고: 리스트의 값을 복제해야 할 때는 deepcopy() 함수를 사용해야한다!