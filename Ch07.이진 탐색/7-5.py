n = int(input())
first = list(map(int, input().split()))
m = int(input())
second = list(map(int, input().split()))

def binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    if array[mid] == target:
      return mid
    elif array[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return None

for i in second:
  answer = binary_search(first, i, 0, n - 1)
  if answer != None:
    print('yes', end = ' ')
  else:
    print('no', end = ' ')
