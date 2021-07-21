n = int(input())
first = list(map(int, input().split()))
m = int(input())
second = list(map(int, input().split()))

for i in second:
  if i in first:
    print('yes', end = ' ')
  else:
    print('no', end = ' ')