word = input()
ans = ''

for w in word:
  if w.islower():
    ans += w.capitalize()
  else:
    ans += w.lower()
print(ans)