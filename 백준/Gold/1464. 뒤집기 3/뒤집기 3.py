import sys
S = list(input())

result = [S[0]]
now = S[0]
for i in range(1, len(S)):
  if now < S[i]:
    result.reverse()
    result.append(S[i])
    result.reverse()
  else:
    now = S[i]
    result.append(S[i])
result.reverse()
print("".join(result))