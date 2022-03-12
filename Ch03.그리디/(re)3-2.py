"""
22-03-12
idea : 가장 큰 수, 그 다음 큰 수를 더하는 횟수를 각각 구한 후, 각 횟수만 큼 더해주기
"""
n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

ans = 0
i, j = (m // k) * k, m % k
ans += arr[-1] * i + arr[-2] * j

print(ans)
