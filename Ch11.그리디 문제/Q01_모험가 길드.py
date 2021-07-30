# 0729
# 모험가 길드
# idea: 모험가 수가 최대 공포도보다 크거나 같으면 그룹으로 묶어준다.
import sys

n = sys.stdin.readline().strip()
arr = sorted(list(map(int, sys.stdin.readline().split())))

# 모험가 수, 그룹의 수 초기화
cnt, ans = 0, 0
for x in arr:
    cnt += 1
    # 모험가 수가 공포도보다 크거나 같을 때 그룹의 수 추가, 모험가 수 초기화
    if x <= cnt:
        ans += 1
        cnt = 0

print(ans)

