# 0724
# 피보나치 함수
# 피보나치 함수(Fibonacci Function)를 재귀 함수로 구현
def fibo(x):
  return 1 if x == 1 or x==2 else fibo(x - 1) + fibo(x - 2)

print(fibo(4))