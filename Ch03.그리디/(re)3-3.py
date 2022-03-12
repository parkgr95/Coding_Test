"""
22-03-12
idea : max, min 함수 사용
"""
n, m = map(int, input().split())
ans = 0

for _ in range(n):
    ans = max(ans, min(list(map(int, input().split()))))

print(ans)

