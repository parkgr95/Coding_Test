# 0724
# idea: 보텀업 방식을 사용해서 각 숫자마다 연산의 최솟값 도출
import sys

x = int(sys.stdin.readline().strip())

d = [0] * 30001

for i in range(2, x+1):
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i-1] + 1
    # 현재의 수에서 2로 나누어 떨어지는 경우
    if d[i] % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    # 현재의 수에서 3을 나누어 떨어지는 경우
    if d[i] % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    # 현재의 수에서 5를 나누어 떨어지는 경우
    if d[i] % 5 == 0:
        d[i] = min(d[i], d[i//5]+1)

print(d[x])