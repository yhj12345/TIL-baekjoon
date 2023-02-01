def find(a):
  if parent[a] == a:
    return a
  parent[a] = find(parent[a])
  return parent[a]

def union(x, y):
  x = find(x)
  y = find(y)

  if x < y:
    parent[y] = x
  else:
    parent[x] = y

n = int(input())
star = [list(map(float, input().split())) for _ in range(n)]
edges = []
for i in range(n):
  for j in range(n):
    if i != j:
      a, b = star[i]
      c, d = star[j]

      dist = (abs(a-c) ** 2 + abs(b-d) ** 2) ** 0.5
      edges.append((i, j, dist))
edges.sort(key=lambda x: x[2])
parent = [i for i in range(n)]
ans = 0
for a, b, dist in edges:
  if find(a) != find(b):
    union(a, b)
    ans += dist
ans = round(ans, 2)
print(ans)