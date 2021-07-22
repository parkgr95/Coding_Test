# 0722
# idea: 정렬 라이브러리를 이용해 리스트를 받으면 각각 오름차순, 내림차순으로 정렬해줌. k번까지 바꿀 수 있으니까 k번동안 a의 작은 값들과 b의 큰 값들을 바꿔줌.
import sys

n, k = map(int, sys.stdin.readline().split())
a = sorted(list(map(int, sys.stdin.readline().split())))
b = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]

print(sum(a))