# 0722
# 삽입 정렬
array = list(map(int, input().split()))
for i in range(1, len(array)):
  for j in range(i, 0, -1): # 인덱스 i부터 1까지 감소하며 반복하는 문법
    if array[j] < array[j - 1]: # 한 칸씩 왼쪽으로 이동
      array[j], array[j - 1] = array[j - 1], array[j]
    else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
      break

print(array)

# 회고: 정렬이 되어있는 경우 퀵정렬보다 강력하다.