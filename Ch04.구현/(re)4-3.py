"""
22-03-15
idea : 나이트가 이동할 수 있는 경로 확인하기
"""
In = input()
y, x = ord(In[0]) - 97, int(In[1])

steps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
ans = 0

for step in steps:
    if 1 <= x + step[0] < 9 and 1 <= y + step[1] < 9:
        ans += 1

print(ans)