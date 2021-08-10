# 0809
# 공유기 설치
# idea: 이진 탐색 함수 사용
import sys

def binary_search(array, start, end):
    answer = 0
    while(start <= end):
        mid = (start+end) // 2 # 가장 인접한 두 공유기 사이의 거리
        value = array[0]
        count = 1
        for i in range(1, n):
            # 앞에서부터 차근차근 설치
            if array[i] >= value + mid:
                value = array[i]
                count += 1
        if count >= c: # c개 이상의 공유기를 설치할 수 있는 경우, 거리를 증가
            start = mid + 1
            answer = mid
        else: # c개 이상의 공유기를 설치할 수 없는 경우, 거리를 감소
            end = mid - 1
    return answer

if __name__ == "__main__":
    n, c = map(int, sys.stdin.readline().split())
    array = sorted([int(sys.stdin.readline().rstrip()) for _ in range(n)])

    start = 1 # 집의 좌표 중에서 가장 작은 값
    end = array[-1] - array[0] # 집의 좌표 중에서 가장 큰 값

    print(binary_search(array, start, end))

# 회고: 답을 보고야 말았다... 예전 7-8 문제인 떡 썰기를 참고하면서 풀어보자.