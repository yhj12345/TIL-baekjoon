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
  

# 크루스칼 
N, M = map(int, input().split())
parent = [i for i in range(N+1)]

god = [list(map(int, input().split())) for _ in range(N)]
edges = []
for i in range(N):
  for j in range(N):
    if i != j:
      a, b = god[i]
      c, d = god[j]
      dist = (abs(a - c) ** 2 + abs(b - d) ** 2) ** 0.5
      edges.append((i+1, j+1, dist))

for i in range(M):
  a, b = map(int, input().split())
  edges.append((a, b, 0))
  edges.append((b, a, 0))

edges.sort(key=lambda x: x[2])
ans = 0
for a, b, dist in edges:
  if find(a) != find(b):
    union(a, b)
    ans += dist

print(f'{ans:.2f}')