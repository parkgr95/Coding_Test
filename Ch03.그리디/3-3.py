# 0721
# idea: 각 행마다 가장 작은 수를 찾은 뒤에 그 수 중에서 가장 큰 수 찾기
import sys

n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, input().split())) for _ in  range(n)]

ans = 0
# 각각의 행들 중 가장 작은 값들을 비교하여 가장 큰 값을 찾기
for a in arr:
  min_ = min(a)
  ans = max(ans, min_)

print(ans)

# 회고: 행을 입력할 때마다 작은 값 뽑아보자

import sys
n, m = map(int, sys.stdin.readline().split())

ans = 0
for i in range(n):
  array = list(map(int, input().split()))
  min_value = min(array)
  result = max(result, min_value)

print(result)