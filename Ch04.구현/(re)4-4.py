"""
22-03-15
idea : 매뉴얼대로 구현
"""
n, m = map(int, input().split())
x, y, d = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited = [[False] * m for _ in range(n)]
visited[x][y] = True
ans = 1  # 방문한 칸의 수
cnt = 0  # 회전 횟수

def turn():
    global d
    d -= 1 if d > 0 else -3

while True:
    turn()
    tx, ty = x + dx[d], y + dy[d]
    if not visited[tx][ty] and not B[tx][ty]:
        x, y = tx, ty
        visited[x][y] = True
        ans += 1
        cnt = 0  # 회전한 다음 전진 하면 다시 1번부터!
        continue
    else:
        cnt += 1  # 회전만 수행
    if cnt == 4:
        nx, ny = x - dx[d], y - dy[d]
        if not B[nx][ny]:
            x, y = nx, ny
            cnt = 0
            continue  # 굳이 필요 없긴 함
        else:
            break

print(ans)