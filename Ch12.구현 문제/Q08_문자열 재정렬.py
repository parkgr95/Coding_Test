# 0731
# 문자열 재정렬
# idea: 문자열에서 문자와 숫자를 구분하여 각각 오름차순으로 정렬하고 숫자들 합한뒤, 모두 합춰서 출력
import sys

s = sys.stdin.readline().strip()

cha = []
num = 0
for x in s:
    if x.isalpha():
        cha.append(x)
    else:
        num += int(x)

cha.sort()

if num != 0:
    cha.append(str(num))

print(''.join(cha))