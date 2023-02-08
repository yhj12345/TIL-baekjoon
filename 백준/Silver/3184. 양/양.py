from collections import deque

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(si, sj):
  q = deque()
  q.append((si, sj))
  visited[si][sj] = True

  s_cnt, w_cnt = 0, 0
  if arr[si][sj] == 'v':
    w_cnt += 1
  elif arr[si][sj] == 'o':
    s_cnt += 1

  while q:
    ti, tj = q.popleft()
    for k in range(4):
      ni = ti + di[k]
      nj = tj + dj[k]
      if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] != '#' and not visited[ni][nj]:
        visited[ni][nj] = True
        q.append((ni, nj))
        if arr[ni][nj] == 'v':
          w_cnt += 1
        elif arr[ni][nj] == 'o':
          s_cnt += 1
  return w_cnt, s_cnt


R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
visited = [[False for _ in range(C)] for _ in range(R)]

wolf, sheep = 0, 0

for i in range(R):
  for j in range(C):
    if not visited[i][j] and arr[i][j] != '#':
      w_tmp, s_tmp = bfs(i, j)
      if w_tmp >= s_tmp:
        wolf += w_tmp
      else:
        sheep += s_tmp
print(sheep, wolf)
