n = int(input())
A = list(map(int, input().split()))
A.sort()
ans = 0
cnt = 0

for a in A:
    cnt += 1
    if cnt >= a:
        ans += 1
        cnt = 0

print(ans)