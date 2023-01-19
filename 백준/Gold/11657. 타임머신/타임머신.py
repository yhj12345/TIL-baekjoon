import sys

def bf(start):
  dist[start] = 0

  for i in range(N):
    for j in range(M):
      node = bus[j][0]
      next_node = bus[j][1]
      cost = bus[j][2]

      if dist[node] != INF and dist[next_node] > dist[node] + cost:
        dist[next_node] = dist[node] + cost

        if i == N-1:
          return True
  return False

N, M = map(int, input().split())
bus = [list(map(int, input().split())) for _ in range(M)]
INF = 1e9
dist = [INF] * (N+1)

is_negative = bf(1)
if is_negative:
  print(-1)
else:
  for i in range(2, N+1):
    if dist[i] == INF:
      print(-1)
    else:
      print(dist[i])