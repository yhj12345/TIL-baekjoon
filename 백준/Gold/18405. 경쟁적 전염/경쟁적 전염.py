import sys
import heapq

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs():
  while q:
    time, virus, ti, tj = heapq.heappop(q)
    if time == S:
      break
    
    for k in range(4):
      ni = ti + di[k]
      nj = tj + dj[k]
      if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
        arr[ni][nj] = virus
        heapq.heappush(q, (time+1, virus, ni, nj))


N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

q = []
for i in range(N):
  for j in range(N):
    if arr[i][j] != 0:
      heapq.heappush(q, (0, arr[i][j], i, j))
bfs()
print(arr[X-1][Y-1])