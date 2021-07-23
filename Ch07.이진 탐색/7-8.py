# 0723
# idea: 이진 탐색을 활용해서 높이 최대가 될때마다 답이 갱신되도록 변환
import sys

# 이진 탐색 함수
def binary_search(array, target, start, end):
    ans = 0
    while start <= end:
        total = 0
        mid = (start+end) // 2
        for x in array:
            if x > mid:
                total += x - mid
        if total < target:
            end = mid - 1
        # 높이의 최댓값을 구하기 위해 최댓값이 답이 될 때마다 답을 갱신
        else:
            ans = mid
            start = mid + 1
    return ans


n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

print(binary_search(arr, m, 0, max(arr)))

# 회고: 처음엔 그냥 이진 탐색 코드를 그대로 사용하였는데 답지와 답이 달라 비교해보니 높이가 최대가 될 때를 구하는 문제이므로 답이 커질수록 갱신하도록 바꿨다. 테스트 케이스가 하나밖에 없어서 기존 코드도 맞는 지를 확인해볼 수가 없어서 답답하다. 여러개가 답이 나올 수가 있나? 