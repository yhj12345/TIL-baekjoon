exp = input()
ans = ''
stack = []

for s in exp:
  if s.isalpha():
    ans += s
  else:
    if s == '(':
      stack.append(s)
    elif s == '*' or s == '/':
      while stack and (stack[-1] == '*' or stack[-1] == '/'):
        ans += stack.pop()
      stack.append(s)
    elif s == '+' or s == '-':
      while stack and stack[-1] != '(':
        ans += stack.pop()
      stack.append(s)
    elif s == ')':
      while stack and stack[-1] != '(':
        ans += stack.pop()
      stack.pop()
while stack:
  ans += stack.pop()
print(ans)