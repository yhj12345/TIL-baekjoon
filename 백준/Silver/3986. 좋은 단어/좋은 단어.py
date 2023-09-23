N = int(input())
ans = 0
for i in range(N):
  word = input()
  stack = []

  for w in word:
    if not stack:
      stack.append(w)
    else:
      if w != stack[-1]:
        stack.append(w)
      else:
        stack.pop()
  
  if not stack:
    ans += 1
print(ans)