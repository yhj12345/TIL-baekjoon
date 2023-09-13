T = int(input())
for tc in range(T):
  n, m = map(int, input().split())
  
  ans = 0

  for i in range(1, n):
    for j in range(1, i):
      a = (i ** 2) + (j ** 2) + m
      b = i * j

      if a % b == 0:
        ans += 1
  print(ans)