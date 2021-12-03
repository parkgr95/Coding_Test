n, m = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for i in range(n):
    for j in range(i, n):
        if A[i] != A[j]:
            ans += 1

print(ans)