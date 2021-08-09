# 0809
# 고정점 찾기
# idea: 이진 탐색 함수 사용
import sys

def binary_search(array, start, end):
    if start > end:
        return None
    mid = (start+end) // 2
    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        return binary_search(array, start, mid-1)
    else:
        return binary_search(array, mid+1, end)

if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    data = list(map(int, sys.stdin.readline().split()))

    print(binary_search(data, 0, n-1))