"""
22-03-12
4회차 반복 시작
idea : 가장 큰 화폐 단위 부터 돈을 거슬러 주기
"""
n = 1260
ans = 0

coin = [500, 100, 50, 10]
for c in coin:
    ans += n // c
    n %= c

print(ans)