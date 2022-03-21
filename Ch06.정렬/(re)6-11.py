"""
22-03-21
idea : 딕셔너리 사용
"""
dic = {}
for _ in range(int(input())):
    n, s = input().split()
    dic[n] = s

d = sorted(dic)
print(d)