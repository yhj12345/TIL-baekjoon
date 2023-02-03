import sys
from collections import deque
input = sys.stdin.readline
def find(a):
  if a == parent[a]:
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

def bfs(start):
  global ans
  q = deque()
  q.append((start, 10 ** 6))
  visited[start] = 1

  while q:
    now, weight = q.popleft()
    if now == e:
      ans = weight
      break
    for node, next_weight in graph[now]:
      if visited[node] == 0:
        visited[node] = 1
        q.append((node, min(next_weight, weight)))

N, M = map(int, input().split())
s, e = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
parent = [i for i in range(N+1)]
graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
edges.sort(key=lambda x: -x[2])

for i, j, wei in edges:
  if find(i) != find(j):
    union(i, j)
    graph[i].append((j, wei))
    graph[j].append((i, wei))

ans = 0
bfs(s)
print(ans)
