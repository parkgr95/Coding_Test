# 0721
import sys

n = int(sys.stdin.readline().split())

# 큰 동전부터 차례대로 확인
money = [500, 100, 50, 10]

ans = 0
for m in money:
  ans += n // m
  n %= m

print(ans)