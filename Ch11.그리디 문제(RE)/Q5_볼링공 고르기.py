n, m = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for i in range(n):
    for j in range(i, n):
        if A[i] != A[j]:
            ans += 1

print(ans)

# 답안지
n, m = map(int, input().split())
data = list(map(int, input().split()))

array = [0] * 11

for x in data:
  array[x] += 1

result = 0
for i in range(1, n + 1):
  n -= array[i]
  result += array[i] * n

print(result)