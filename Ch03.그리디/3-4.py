# 0721
# idea: 최대한 많이 나누기
import sys

n, k = map(int, sys.stdin.readline().split())

ans = 0
while n != 1:
    if n % k == 0:
        n //= k
    else:
        n -= 1
    ans += 1

print(ans)