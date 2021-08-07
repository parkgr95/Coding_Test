# 0804
# 괄호 변환
# idea: dfs

import sys

def dfs(i, now):
    global max_, min_, add, sub, mul, div
    if i == n:
        max_ = max(max_, now)
        min_ = min(min_, now)
    else:
        # 각 연산자에 대하여 재귀적으로 수행
        if add > 0:
            add -= 1
            dfs(i+1, now+arr[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1, now-arr[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i+1, now*arr[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1, int(now/arr[i]))
            div += 1

if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    arr = list(map(int, sys.stdin.readline().split()))
    add, sub, mul, div = map(int, sys.stdin.readline().split())
    max_, min_, = -1e9, 1e9

    dfs(1, arr[0])

    print(max_)
    print(min_)

# 회고: 자료형 신경 쓰자 ^^. int를 안써서 30분동안 해매는 일 없게 ^^