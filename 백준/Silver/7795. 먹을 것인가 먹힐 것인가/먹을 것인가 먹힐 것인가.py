import sys
from bisect import bisect_left

T = int(input())
for _ in range(T):
  N, M = map(int, input().split())
  A = list(map(int, input().split()))
  B = list(map(int, input().split()))

  A.sort()
  B.sort()
  result = 0
  for i in A:
    result += bisect_left(B, i)
  print(result)