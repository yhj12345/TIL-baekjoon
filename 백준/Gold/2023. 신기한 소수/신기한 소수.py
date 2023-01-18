import math

def is_prime_number(x):
  for i in range(2, int(x ** 0.5)+1):
    if x % i == 0:
      return False
  return True
    

def dfs(number, depth):
  if is_prime_number(number) == False:
    return
  if depth == N:
    print(number)
    return
  for k in range(10):
    dfs(number*10 + k, depth+1)

N = int(input())
for i in range(2, 10):
  dfs(i, 1)