# 0729
# 곱하기 혹은 더하기
# idea: 숫자가 0 or 1이면 더해주고 아니면 곱해준다.
import sys

s = sys.stdin.readline().rstrip()

ans = int(s[0])
for x in s[1:]:
    if ans <= 1 or int(x) <= 1:
        ans += int(x)
    else:
        ans *= int(x)

print(ans)

# 회고: 현재 답 0일 경우 그 다음수가 1보다 크면 곱을 하므로 조건에 현재 답이 0이나 1보다 작을 경우를 넣어줘야 한다.