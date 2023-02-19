import sys
from collections import deque
input = sys.stdin.readline

def find(x):
  if x == parent[x]:
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

def bfs(start):
  visited = [0 for _ in range(N+1)]
  depth = 0
  result = 0
  visited[start] = 1
  q = deque()
  q.append(start)

  while q:
    now = q.popleft()
    for next, dist in graph[now]:
      if visited[next] == 0:
        visited[next] = 1
        result += dist + (t * depth)
        depth += 1
        q.append(next)
  return result

N, M, t = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
edges.sort(key=lambda x: x[2])
parent = [i for i in range(N+1)]
graph = [[] for _ in range(N+1)]

for a, b, cost in edges:
  if find(a) != find(b):
    graph[a].append((b, cost))
    graph[b].append((a, cost))
    union(a, b)

answer = bfs(1)
print(answer)