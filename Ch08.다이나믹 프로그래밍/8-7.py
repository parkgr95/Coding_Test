# 0724
# idea: 2xn 크기의 바닥을 채우는 경우의 수는 n-1일때와 n-2일때 경우의 수의 합이다. n-1일때에는 2x1만 올 수 있고, n-2일때는 1x2, 2x2인 2가지가 올 수 있다.
import sys

n = int(sys.stdin.readline().strip())

d = [0] * 1001

d[1] = 1
d[2] = 3

for i in range(3, n+1):
    # 방법의 수를 796,796으로 나눈 나머지
    d[i] = (d[i-1] + 2*d[i-2]) % 796796

print(d[n])