# 0803
# 치킨 배달
# idea: 조합 라이브러리를 사용해 완전 탐색
import sys
from itertools import combinations

# 도시의 치킨 거리의 최솟값 찾기
def find_min(house, chicken):
    distance = 0
    for h in house:
        # 각 집의 치킨 거리 구하기
        distance += min([abs(h[0]-c[0])+abs(h[1]-c[1]) for c in chicken])
    return distance

if __name__ == "__main__":

    n, m = map(int, sys.stdin.readline().split())

    # 집과 치긴집의 위치정보 담기
    house, chicken = [], []
    for i in range(n):
        graph = list(map(int, sys.stdin.readline().split()))
        for j in range(n):
            if graph[j] == 1: house.append((i, j))
            elif graph[j] == 2: chicken.append((i, j))

    # 치킨집을 m개 골랐을 때, 도시의 치킨 거리의 최솟값 출력
    answer = sys.maxsize
    for cb in combinations(chicken, m):
        # 조합들의 치킨 거리 중에서 최솟값 구하기
        answer = min(answer, find_min(house, cb))
    print(answer)