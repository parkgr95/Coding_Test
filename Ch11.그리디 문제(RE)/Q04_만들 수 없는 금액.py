n = int(input())
A = list(map(int, input().split()))
A.sort()
ans = 1
for a in A:
    if ans < a:
        break
    ans += a
print(ans)