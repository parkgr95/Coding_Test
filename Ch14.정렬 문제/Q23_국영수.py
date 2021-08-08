# 0808
# 국영수
# idea: 정렬 함수 사용
import sys

if __name__ == "__main__":
    array = [list(sys.stdin.readline().split()) for _ in range(int(sys.stdin.readline().rstrip()))]

    array.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
    for a in array:
        print(a[0])