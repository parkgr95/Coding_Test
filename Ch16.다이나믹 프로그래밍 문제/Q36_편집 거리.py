# 0809
# 편집 거리
# idea: 다이나믹 프로그래밍
import sys

def edit_dist(str1, str2):
    n, m = len(str1), len(str2)

    d = [[0] * (m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        d[i][0] = i
    for j in range(1, m+1):
        d[0][j] = j

    for i in range(1, n+1):
        for j in range(1, m+1):
            if str1[i-1] == str2[j-1]:
                d[i][j] = d[i-1][j-1]
            else:
                d[i][j] = 1 + min(d[i][j-1], d[i-1][j], d[i-1][j-1]) # 삽입(왼쪽), 삭제(위쪽), 교체(왼쪽 위)

    return d[n][m]

if __name__ == "__main__":
    str1, str2 = str(sys.stdin.readline().rstrip()), str(sys.stdin.readline().rstrip())
    print(edit_dist(str1, str2))