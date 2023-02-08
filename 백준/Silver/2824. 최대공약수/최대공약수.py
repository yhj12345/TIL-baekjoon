from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

dict_A = defaultdict(int)
dict_B = defaultdict(int)
set_A = set()
set_B = set()

for i in range(N):
  a_num = A[i]
  for j in range(2, int(A[i] ** 0.5) + 1):
    while a_num % j == 0:
      dict_A[j] += 1
      set_A.add(j)
      a_num //= j
  if a_num != 1:
    dict_A[a_num] += 1
    set_A.add(a_num)
for i in range(M):
  b_num = B[i]
  for j in range(2, int(B[i] ** 0.5) + 1):
    while b_num % j == 0:
      dict_B[j] += 1
      set_B.add(j)
      b_num //= j
  if b_num != 1:
    dict_B[b_num] += 1
    set_B.add(b_num)

set_AB = set_A & set_B
ans = 1
for number in set_AB:
  if dict_A[number] <= dict_B[number]:
    ans *= number ** dict_A[number]
  else:
    ans *= number ** dict_B[number]

print(str(ans)[-9:])