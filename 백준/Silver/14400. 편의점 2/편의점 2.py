n = int(input())
x = []
y = []

for _ in range(n):
  a, b = map(int, input().split())
  x.append(a)
  y.append(b)

x.sort()
y.sort()

mid_x = x[n//2]
mid_y = y[n//2]

ans = 0

for i in range(n):
  ans += (abs(mid_x - x[i]) + abs(mid_y - y[i]))

print(ans)