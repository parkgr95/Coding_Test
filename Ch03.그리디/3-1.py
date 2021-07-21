# 0721
# idea: '가장 큰 화폐 단위부터' 돈을 거슬러 주기
import sys

n = int(sys.stdin.readline().split())

# 큰 동전부터 차례대로 확인
money = [500, 100, 50, 10]

ans = 0
for m in money:
  ans += n // m
  n %= m

print(ans)