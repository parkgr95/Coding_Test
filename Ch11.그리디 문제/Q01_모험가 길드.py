n = int(input())
data = list(map(int, input().split()))
data.sort()

count = 0 # 모험가의 수
result = 0 # 그룹의 수

for x in data:
 count += 1
 if x <= count:
   result += 1
   count = 0

print(result) 