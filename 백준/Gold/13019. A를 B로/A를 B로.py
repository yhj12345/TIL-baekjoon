import sys
from collections import defaultdict

A = list(input())
B = list(input())

dict_a = defaultdict(int)
dict_b = defaultdict(int)
for i in range(len(A)):
  dict_a[A[i]] += 1
  dict_b[B[i]] += 1

flag = True
for i in dict_a:
  if dict_a[i] != dict_b[i]:
    flag = False
    break
if flag == False:
  print(-1)
else:
  ans = 0
  tmp = len(A) - 1
  for i in range(len(A)-1, -1, -1):
    if A[i] != B[tmp]:
      ans += 1
    else:
      tmp -= 1
  print(ans)