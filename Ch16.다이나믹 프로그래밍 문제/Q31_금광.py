# 0809
# 금광
# idea: 다이나믹 프로그래밍
import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    n, m = map(int, sys.stdin.readline().split())
    array = list(map(int, sys.stdin.readline().split()))

    d = []
    i = 0
    for _ in range(n):
        d.append(array[i:i + m])
        i += m

    for j in range(1, m):
        for i in range(n):
            if i == 0:  # 위일 경우
                left_up = 0
            else:
                left_up = d[i - 1][j - 1]
            if i == n - 1:  # 아래일 경우
                left_down = 0
            else:
                left_down = d[i + 1][j - 1]
            left = d[i][j - 1] # 바로 옆일 경우
            d[i][j] = d[i][j] + max(left_up, left_down, left)

    result = 0
    for i in range(n):
        result = max(result, d[i][m - 1])

    print(result)


