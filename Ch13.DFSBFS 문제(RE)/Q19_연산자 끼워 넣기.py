def dfs(i, now):
    global max_, min_, add, sub, mul, div
    if i == n:
        max_ = max(max_, now)
        min_ = min(min_, now)
    else:
        if add:
            add -= 1
            dfs(i + 1, now + arr[i])
            add += 1
        if sub:
            sub -= 1
            dfs(i + 1, now - arr[i])
            sub += 1
        if mul:
            mul -= 1
            dfs(i + 1, now * arr[i])
            mul += 1
        if div:
            div -= 1
            dfs(i + 1, int(now / arr[i]))
            div += 1

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    add, sub, mul, div = map(int, input().split())

    max_, min_ = -1e9, 1e9
    dfs(1, arr[0])
    print(max_)
    print(min_)