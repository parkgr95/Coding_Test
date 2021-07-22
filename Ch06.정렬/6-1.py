# 0722
# idea: 스와프 사용. 스와프: 두 변수의 위치를 변경하는 작업
# 선택 정렬
import sys

array = list(map(int, sys.stdin.readline().split()))

for i in range(len(array)):
  min_index = i # 가장 작은 원소의 인덱스
  for j in range(i + 1, len(array)):
    if array[min_index] > array[j]:
      min_index = j
  array[i], array[min_index] = array[min_index], array[i] # 스와프

print(array) 