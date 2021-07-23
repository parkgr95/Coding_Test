# 0723
# idea: 이진 탐색으로 풀어보기
import sys

# 이진 탐색 함수
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == target:
            return True
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False

n = int(sys.stdin.readline().strip())
# 가게의 부품 정렬
arr1 = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline().strip())
# 손님의 부품
arr2 = list(map(int, sys.stdin.readline().split()))

# 손님이 원하는 부품이 있는 지 하나씩 확인
for x in arr2:
    print('yes', end=' ') if binary_search(arr1, x, 0, n-1) else print('no', end=' ')

# 회고: 최대한 간결하게 작성해보았다. 이진 탐색을 위해서 정렬을 해야하는 데 필요한 시간 복잡도 O(N*logN)와 이진 탐색에 걸리는 시간 복잡도 O(M*logN)를 합해 총 시간 복잡도는 O((M + N)*logN)이었다. 1000만 미만에서는 집합 자료형으로 푸는 게 괜찮을 지도...? 그래도 연습을 계속 해봐야겠다.