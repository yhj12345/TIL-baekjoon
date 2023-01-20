from collections import deque

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def dfs(si, sj, depth):
  global cnt
  if depth == K:
    if si == 0 and sj == C-1:
      cnt += 1
    return 
  for k in range(4):
    ni = si + di[k]
    nj = sj + dj[k]
    if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] != 'T' and visited[ni][nj] == 0:
      visited[ni][nj] = 1
      dfs(ni, nj, depth+1)
      visited[ni][nj] = 0



R, C, K = map(int ,input().split())
arr = [list(input()) for _ in range(R)]
visited = [[0 for _ in range(C)] for _ in range(R)]
visited[R-1][0] = 1
cnt = 0
dfs(R-1, 0, 1)
print(cnt)