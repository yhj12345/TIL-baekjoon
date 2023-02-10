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
  alpha = defaultdict(int)
  cnt = 0
  A_idx = len(A) - 1
  while True:
    if cnt == len(A):
      break
    next = A[A_idx]
    alpha[next] += 1
    tmp = 0
    B_idx = 0
    for i in range(len(B)-1, -1, -1):
      if next == B[i]:
        tmp += 1
        if tmp == alpha[next]:
          B_idx = i
          break
    if B_idx < A_idx:
      a = A.pop(A_idx)
      A.insert(0, a)
      alpha[next] -= 1

      cnt += 1
      ans += 1
    else:
      A_idx -= 1
      cnt += 1
  print(ans)