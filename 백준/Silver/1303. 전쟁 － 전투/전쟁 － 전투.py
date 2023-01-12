import sys
from collections import deque

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(si, sj, color):
  visited[si][sj] = 1
  q = deque()
  q.append((si, sj))
  cnt = 1

  while q:
    ti, tj = q.pop()
    for k in range(4):
      ni = ti + di[k]
      nj = tj + dj[k]
      if 0 <= ni < M and 0 <= nj < N and visited[ni][nj] == 0 and color == arr[ni][nj]:
        q.append((ni, nj))
        visited[ni][nj] = 1
        cnt += 1
  return cnt


N, M = map(int ,input().split())
arr = [list(input()) for _ in range(M)]
visited = [[0 for _ in range(N)] for _ in range(M)]

white = 0
blue = 0
for i in range(M):
  for j in range(N):
    if visited[i][j] == 0:
      if arr[i][j] == 'B':
        soldier = bfs(i, j, 'B')
        blue += soldier ** 2
      else:
        soldier = bfs(i, j, 'W')
        white += soldier ** 2
print(white, blue)