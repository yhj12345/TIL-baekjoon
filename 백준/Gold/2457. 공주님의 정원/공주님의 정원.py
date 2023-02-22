N = int(input())
arr = []
for _ in range(N):
  a, b, c, d = map(int, input().split())
  start = (100*a) + b
  end = (100*c) + d
  arr.append((start, end))
arr.sort(key=lambda x: (-x[0], -x[1]))

ans = 0
start = 0
end = 301

while arr:
  if end >= 1201 or end < arr[-1][0]:
    break
  while arr:
    if end < arr[-1][0]:
      break
    else:
      if start <= arr[-1][1]:
        start = arr[-1][1]
      arr.pop()

  end = start
  ans += 1
if end >= 1201:
  print(ans)
else:
  print(0)