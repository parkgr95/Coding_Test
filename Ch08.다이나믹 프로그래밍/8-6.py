# 0724
# idea: 보텀업 방식을 사용해서 d[n-1]의값과 d[n-2]와 arr[n]의 최댓값을 비교
import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))

d = [0] * 100

d[0] = arr[0]
d[1] = max(arr[0], arr[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + arr[i])

print(d[n-1])

# 회고: 배열이 주어지면 dp테이블의 n값을 배열의 n값과 맞춰주는 게 좋은 것다.