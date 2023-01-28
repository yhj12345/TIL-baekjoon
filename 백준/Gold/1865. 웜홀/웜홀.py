def bf(start):
  dist[start] = 0
  for i in range(1, N+1):
    for j in range(1, N+1):
      for next, time in graph[j]:
        if dist[next] > dist[j] + time:
          dist[next] = dist[j] + time
          if i == N:
            return True
  return False

TC = int(input())
for tc in range(1, TC+1):
  N, M, W = map(int, input().split())
  
  graph = [[] for _ in range(N+1)]
  dist = [10001 for _ in range(N+1)]
  for m in range(M):
    S, E, T = map(int, input().split())
    graph[S].append([E, T])
    graph[E].append([S, T])
  
  for w in range(W):
    S, E, T = map(int, input().split())
    graph[S].append([E, -T])
  
  negative_cycle = bf(1)
  if not negative_cycle:
    print("NO")
  else:
    print("YES")