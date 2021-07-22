# 0721
# idea: 기본 리스트에서 append()와 pop()를 이용
# 스택
# 선입후출(FILO) or 후입선출(LIFO)
stack = []

# 삽입(5) - 삽입(2) - 삽입(3) -삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) # 최하단 원소부터 출력
print(stack[::-1]) # 최상단 원소부터 출력