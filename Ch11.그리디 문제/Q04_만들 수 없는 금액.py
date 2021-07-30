# 0729
# 만들 수 없는 금액
# idea: 1부터 차례대로 특정한 금액을 만들 수 있는 지 확인한다.
import sys

n = sys.stdin.readline().strip()
arr = sorted(list(map(int, sys.stdin.readline().split())))

ans = 1
for x in arr:
    if ans < x:
        break
    ans += x

print(ans)

# 회고: 아직도 알고리즘이 이해가지 않았나보다... 그리디 알고리즘은 현재 상태에서 매번 가장 좋아 보이는 것만을 선택하는 알고리즘이다. 이걸 응용해서 현재 상태를 '1부터 target-1까지의 모든 금액을 만들 수 있는 상태'라고 보자!