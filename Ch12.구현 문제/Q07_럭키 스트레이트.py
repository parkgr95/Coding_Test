# 0731
# 럭키 스트레이트
# idea: 주어진 n을 절반으로 나누어 각각의 합을 비교해준다.
import sys

n = sys.stdin.readline().strip()

l_sum, r_sum = 0, 0
for i in range(len(n)//2):
    l_sum += int(n[i])
    r_sum += int(n[-i-1])

print("LUCKY") if l_sum == r_sum else print("READY")

# 회고: 하나의 변수를 초기화 해준뒤 앞의 값을 더해준 뒤 뒤의 값을 빼주는 식으로 만들면 공간 복잡도가 더 좋을 것 같다.