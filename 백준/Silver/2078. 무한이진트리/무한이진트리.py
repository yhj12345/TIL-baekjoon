import sys

A, B = map(int, input().split())
L, R = 0, 0
while True:
  if A == 1 and B == 1:
    break

  if A > B:
    L += 1
    A -= B
  else:
    R += 1
    B -= A

print(L, R)