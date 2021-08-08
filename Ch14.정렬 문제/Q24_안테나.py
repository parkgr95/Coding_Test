# 0808
# 안테나
# idea: 정렬 함수 사용
import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    array = sorted(list(map(int, sys.stdin.readline().split())))
    # 가운데일 수록 모든 거리와 최소
    print(array[(n-1)//2])
