n = int(input())
first = [0] * 10001

for i in input().split():
  first[int(i)] = 1

m = int(input())
second = list(map(int, input().split()))

for i in second:
  if first[i] == 1:
    print('yes', end = ' ')
  else:
    print('no', end = ' ')