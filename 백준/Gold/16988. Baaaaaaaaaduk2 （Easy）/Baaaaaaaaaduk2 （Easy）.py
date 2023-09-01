from collections import deque
from itertools import combinations

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def copy_arr():
  new_arr = [[0 for _ in range(M)] for _ in range(N)]
  for i in range(N):
    for j in range(M):
      new_arr[i][j] = arr[i][j]
  return new_arr

def bfs(si, sj):
  visited[si][sj] = 1
  q = deque()
  q.append((si, sj))
  cnt = 1
  flag = False

  while q:
    ti, tj = q.popleft()

    for k in range(4):
      ni = ti + di[k]
      nj = tj + dj[k]

      if 0 > ni or ni >= N or 0 > nj or nj >= M or visited[ni][nj]:
        continue

      if new_arr[ni][nj] == 2:
        q.append((ni, nj))
        visited[ni][nj] = 1
        cnt += 1
      elif new_arr[ni][nj] == 0:
        flag = True
      
  return cnt if not flag else -1

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
empty = []
for i in range(N):
  for j in range(M):
    if arr[i][j] == 0:
      empty.append((i, j))

ans = 0

for combi in combinations(empty, 2):
  new_arr = copy_arr()
  for x, y in combi:
    new_arr[x][y] = 1
  
  visited = [[0 for _ in range(M)] for _ in range(N)]
  total = 0

  for i in range(N):
    for j in range(M):
      if visited[i][j] == 0 and new_arr[i][j] == 2:
        cnt = bfs(i, j)
        if cnt != -1:
          total += cnt
  
  ans = max(ans, total)
print(ans)