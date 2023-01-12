import sys

N, M, K = map(int, input().split())
arr = [[0 for _ in range(N+1)] for _ in range(N+1)]

for _ in range(K):
  a, b, c = map(int, input().split())
  if a < b:
    arr[a][b] = max(arr[a][b], c)

dp = [[0 for _ in range(N+1)] for _ in range(M+1)]

for i in range(2, N+1):
  dp[2][i] = arr[1][i]

for i in range(3, M+1):
  for j in range(i, N+1):
    for k in range(2, j):
      if dp[i-1][k] != 0 and arr[k][j] != 0:
        dp[i][j] = max(dp[i-1][k] + arr[k][j], dp[i][j])

result = 0
for i in range(M+1):
  result = max(dp[i][N], result)
print(result)