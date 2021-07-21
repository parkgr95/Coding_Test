# 0721
import sys

n, m, k = map(int, sys.stdin.readline().split())
arr = sorted(list(map(int, sys.stdin.readline().split())))

# 총 m번 중 가장 큰 수가 들어가는 횟수
cnt = m // k * k
ans = 0
ans += cnt * arr[-1]
ans += (m-cnt) * arr[-2]

print(ans)