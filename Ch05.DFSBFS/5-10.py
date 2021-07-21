# 0721
# idea: dfs를 이용해 연결되어 있는 노드들의 묶음을 찾아 준다.
import sys

n, m = map(int, sys.stdin.readline().split())
# strip(): 문자열 맨 앞과 맨 끝의 공백문자를 제거
arr = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

def dfs(x, y):
    # 공간을 벗어나지 않고 방문하지 않았다면 방문
    if 0 <= x < n and 0 <= y < m and not arr[x][y]:
        # 방문 처리
        arr[x][y] = 1
        # 상, 하, 좌, 우
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

ans = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            ans += 1
print(ans)

# 회귀: 처음에 무지성으로 visited를 썻지만, 어차피 그래프에서 0을 지워가며 방문 처리를 하므로 필요가 없다.