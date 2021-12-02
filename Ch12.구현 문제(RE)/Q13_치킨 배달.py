from itertools import combinations

def find_min(house, chicken):
    res = 0
    for h in house:
        res += min([abs(h[0] - c[0]) + abs(h[1] - c[1]) for c in chicken])
    return res

if __name__ == "__main__":
    n, m = map(int, input().split())
    house, chicken = [], []
    for i in range(n):
        B = list(map(int, input().split()))
        for j in range(n):
            if B[j] == 1:
                house.append((i, j))
            elif B[j] == 2:
                chicken.append((i, j))

    ans = int(1e9)
    for cb in combinations(chicken, m):
        ans = min(ans, find_min(house, cb))
    print(ans)