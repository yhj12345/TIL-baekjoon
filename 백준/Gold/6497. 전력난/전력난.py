import heapq

def prim(graph, start):
  result = 0
  q = []
  heapq.heappush(q, (0, start))

  while q:
    cost, t = heapq.heappop(q)
    if not visited[t]:
      result += cost
      visited[t] = True
      for next_cost, next in graph[t]:
        if not visited[next]:
          heapq.heappush(q, (next_cost, next))
  return result

while True:
  m, n = map(int, input().split())
  if m == 0 and n==0:
    break

  total_cost = 0
  graph = [[] for _ in range(m)]
  visited = [False] * m
  for i in range(n):
    x, y, z = map(int, input().split())
    total_cost += z
    graph[x].append((z, y))
    graph[y].append((z, x))
  
  result = prim(graph, 0)
  print(total_cost - result)