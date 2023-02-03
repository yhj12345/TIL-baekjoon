def cal(idx):
  W1, W2 = 0, 0
  for i in range(idx-1, -1, -1):
    if visited[i] == 0:
      W1 = W[i]
      break
  for i in range(idx+1, N):
    if visited[i] == 0:
      W2 = W[i]
      break
  return W1 * W2

def dfs(depth):
  global ans
  if depth == N-2:
    ans = max(ans, sum(result))
    return
  for i in range(1, N-1):
    if visited[i] == 0:
      visited[i] = 1
      result[i] = cal(i)
      dfs(depth+1)
      visited[i] = 0
      result[i] = 0

N = int(input())
W = list(map(int, input().split()))
visited = [0 for _ in range(N)]
result = [0 for _ in range(N)]
ans = 0
dfs(0)
print(ans)