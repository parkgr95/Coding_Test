# 0721
import sys

n = int(sys.stdin.readline())

ans = 0
# 시각을 1씩 증가시킬 때 3이 포함되는 지 확인
for i in range(n+1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i) + str(j) + str(k):
        ans += 1

print(ans)