from itertools import permutations


A, B = map(int, input().split())
a = list(str(A))

answer = -1
for permu in permutations(a, len(a)):
  if permu[0] == '0':
    continue

  C = int(''.join(permu))
  if C < B:
    answer = max(answer, C)
print(answer)