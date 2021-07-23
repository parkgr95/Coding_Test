# 0723
# idea: 계수 정렬로 풀어보기
import sys

n = int(sys.stdin.readline().strip())
arr1 = [0]*(10000001)
# 가게의 부품 번호를 받아 입력
for i in sys.stdin.readline().split():
    arr1[int(i)] = 1
m = int(sys.stdin.readline().strip())
# 손님의 부품
arr2 = list(map(int, sys.stdin.readline().split()))

# 손님이 원하는 부품이 있는 지 하나씩 확인
for x in arr2:
    print('yes', end=' ') if arr1[x] == 1 else print('no', end=' ')

# 회고: 계수 정렬로도 풀어봤는데... 너무 메모리의 낭비가 심한 것 같다. n의 범위가 작으면 몰라도 굳이 사용하진 않을 것 같다.