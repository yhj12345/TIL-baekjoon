def dfs(start, cnt, depth):
  global result
  if depth == N:
    result = min(result, cnt)
    return

  for i in range(N):
    if visited[i] == 0:
      visited[i] = 1
      dfs(i, cnt+arr[start][i], depth+1)
      visited[i] = 0

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [0 for _ in range(N)]
for k in range(N):
  for i in range(N):
    for j in range(N):
      arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])
result = 10000000
visited[K] = 1
dfs(K, 0, 1)
print(result)