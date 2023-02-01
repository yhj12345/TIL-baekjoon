def find(x):
  if parent[x] == x:
    return x
  parent[x] = find(parent[x])
  return parent[x]

def union(x, y):
  x = find(x)
  y = find(y)
  if x < y:
    parent[y] = x
  else:
    parent[x] = y


V, E = map(int ,input().split())
edges = [list(map(int, input().split())) for _ in range(E)]
edges.sort(key=lambda x: x[2])
parent = [i for i in range(V+1)]

ans = 0
for a, b, cost in edges:
  if find(a) != find(b):
    union(a, b)
    ans += cost
print(ans)