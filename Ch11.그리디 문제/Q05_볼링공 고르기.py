# 0729
# 볼링공 고르기
# idea: n의 개수가 1,000개 이하이므로 조합 함수를 사용해 조합을 구한 뒤 같은 무게 조합을 제외한 수를 구한다.
import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
arr = sorted(list(map(int, sys.stdin.readline().split())))
comb = combinations(arr, 2)

ans = 0
for c in comb:
    if c[0] == c[1]:
        continue
    ans += 1

print(ans)

# 답안지
n, m = map(int, input().split())
data = list(map(int, input().split()))

array = [0] * 11

for x in data:
  array[x] += 1

result = 0
for i in range(1, n + 1):
  n -= array[i]
  result += array[i] * n

print(result)

# 회고: 답안지의 경우 직접 조합을 구해서 더해줬다. 그리디 알고리즘 방식에 익숙해져보자.