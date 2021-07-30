# 0729
# 문자열 뒤집기
# idea: 필요한 뒤집는 횟수들을 비교해서 그 중 최소의 값을 출력한다.
import sys

s = sys.stdin.readline().rstrip()

c_0 = 0 # 1을 0으로 바꾸는 횟수
c_1 = 0 # 0을 1로 바꾸는 횟수

if int(s[0]) == 0:
    c_1 += 1
else:
    c_0 += 1

for i in range(1, len(s)):
    # 이전 수와 다른 수 일땐
    if s[i] != s[i-1]:
        if int(s[i]) == 0:
            c_1 += 1
        else:
            c_0 += 1

print(min(c_0, c_1))