import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, end, trace):
  q = deque()
  q.append((start, 0, []))
  visited = [0 for _ in range(N+1)]
  visited[start] = 1

  while q:
    now, cnt, tmp = q.popleft()
    if now == end:
      return tmp
    for node in graph[now]:
      if node in trace:
        continue
      if visited[node] == 0:
        q.append((node, cnt+1, tmp+[node]))
        visited[node] = 1

N, M = map(int, input().split())
edges = []
for i in range(M):
  a, b = map(int,input().split())
  if a > b:
    edges.append((b, a))
  else:
    edges.append((a, b))
edges.sort(key=lambda x: (x[0], x[1]))

S, E = map(int, input().split())

graph = [[] for _ in range(N+1)]
answer = 0
for a, b in edges:
  graph[a].append(b)
  graph[b].append(a)

a = bfs(S, E, [])
answer += len(a)

result = bfs(E, S, a)
answer += len(result)
print(answer)