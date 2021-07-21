# 0721
# idea: 경우의 수가 적은 경우 직접 입력
import sys

n = sys.stdin.readline()
x = int(n[1])
# 아스키코드를 참고해서 문자를 해당 숫자로 바꿔준다. ex) 'a' -> 1
y = int(ord(n[0])) - 96

# 이동할 수 있는 8가지 방향
move = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

ans = 0
for m in move:
  nx = x + m[0]
  ny = y + m[1]
  # 이동
  if 1 <= nx <= 8 and 1 <= ny <= 8:
    ans += 1

print(ans)