# 0724
# idea: 보텀업 방식을 이용.
import sys

n, m = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline().strip()) for _ in range(n)]

d = [10001] * 10001

d[0] = 0
for i in range(n):
    # 화폐 가치마다 확인
    for j in range(arr[i], m+1):
        # j-arr[i]을 만드는 방법이 존재한다면
        if d[j-arr[i]] != 10001:
            d[j] = min(d[j], d[j-arr[i]]+1)

print(d[m] if d[m] != 10001 else -1)

# 회고: 결국 책을 보고 말았다... 차례대로 만들 수 있는 최소한의 화폐 개수를 찾아야 한다. 점화식을 먼저 만들어보자