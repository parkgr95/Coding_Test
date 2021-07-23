# 0723
# idea: 집합 자료형을 이용하여 하나씩 확인
import sys

n = int(sys.stdin.readline().strip())
# 가게의 부품
arr1 = set(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().strip())
# 손님의 부품
arr2 = list(map(int, sys.stdin.readline().split()))

# 손님이 원하는 부품이 있는 지 하나씩 확인
for x in arr2:
    print('yes', end=' ') if x in arr1 else print('no', end=' ')

# 회고: 가장 먼저 생각한 코드. 가장 간결한 것 같아서 마음에 든다. 시간 복잡도를 생각하면 n이 1000만개 미만일때 사용하면 좋을 것 같다.