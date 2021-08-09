# 0809
# 정렬된 배열에서 특정 수의 개수 구하기
# idea: 이진 탐색 함수 사용 or 이진 탐색 라이브러리 사용
import sys

# 처음 위치를 찾는 이진 탐색 메서드
def first(array, target, start, end):
    if start > end:
        return n
    mid = (start + end) // 2
    # 해당 값을 가지는 원소 중에서 가장 왼쪽에 있는 경우에만 인덱스 반환
    if (mid == 0 or target > array[mid-1]) and array[mid] == target:
        return mid
    elif array[mid] > target:
        return first(array, target, start, mid-1)
    else:
        return first(array, target, mid+1, end)

# 마지막 위치를 찾는 이진 탐색 메서드
def last(array, target, start, end):
    if start > end:
        return n
    mid = (start + end) // 2
    # 해당 값을 가지는 원소 중에서 가장 오른쪽에 있는 경우에만 인덱스 반환
    if (mid == n-1 or target < array[mid+1]) and array[mid] == target:
        return mid
    elif array[mid] >= target:
        return last(array, target, start, mid-1)
    else:
        return last(array, target, mid+1, end)

if __name__ == "__main__":
    n, x = map(int, sys.stdin.readline().split())
    array = list(map(int, sys.stdin.readline().split()))

    answer = last(array, x, 0, n-1) - first(array, x, 0, n-1)
    print(-1) if answer == 0 else print(answer-1)

# bisect 라이브러리 사용
import sys
from bisect import bisect_left, bisect_right

n, x = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

answer = bisect_right(array, x) - bisect_left(array, x)
print(-1) if answer == 0 else print(answer)