import sys
S = input()
T = input()

subset = set()
for i in range(len(S)):
  for j in range(len(S) - i):
    subset.add(S[j:i+j+1])

result = 0
tmp = ''
for i in T:
  tmp += i
  if tmp not in subset:
    result += 1
    tmp = i
print(result+1)