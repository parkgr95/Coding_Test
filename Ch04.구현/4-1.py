# 0721
# idea: 시뮬레이션, dx, dy로 이동할 방향을 기록
import sys

n = int(sys.stdin.readline())
arr = sys.stdin.readline()

# 좌, 우, 상, 하
move = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

x, y = 1, 1
for a in arr:
  for i in range(4):
    if a == move[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  # 공간을 벗어나면 무시.
  if nx < 1 or nx < 1 or nx > n or ny > n:
    continue 
  x, y = nx, ny

print(x, y)

# 회고: 공간을 벗어나면 무시해야하는 데 벗어남에도 값이 갱신이 됐다. 해당 이동의 수행 자체를 무시해야 하므로, for문과 같은 라인에 맞춰야한다.