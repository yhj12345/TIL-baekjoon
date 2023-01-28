from collections import deque

def bfs(start):
  q = deque()
  visited = [0 for _ in range(N)]
  visited[start] = 1
  q.append(start)
  while q:
    a = q.popleft()
    if a == E:
      return True
    for k in graph[a]:
      if visited[k] == 0:
        q.append(k)
        visited[k] = 1
  return False


def bf():
  for i in range(N):
    for j in range(R):
      now = edges[j][0]
      next = edges[j][1]
      cost = edges[j][2]
      if dist[now] != 100000000 and dist[now] + cost - money[next] < dist[next]:
        dist[next] = dist[now] + cost - money[next]
        if i == N-1:
          if bfs(next):
            return True
  return False


N, S, E, R = map(int, input().split())
edges = []
graph = [[] for _ in range(N)]

for i in range(R):
  tmp = list(map(int, input().split()))
  edges.append(tmp)
  graph[tmp[0]].append(tmp[1])

money = list(map(int, input().split()))
dist = [100000000 for _ in range(N)]
dist[S] = -money[S]
negative_cycle = bf()
if dist[E] == 100000000:
  print('gg')
else:
  if negative_cycle:
    print('Gee')
  else:
    print(-dist[E])