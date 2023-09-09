N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[[0, 0, 0] for _ in range(N+1)] for _ in range(N+1)]
dp[1][2][0] = 1

for i in range(1, N+1):
  for j in range(1, N+1):
    if arr[i-1][j-1] == 1:
      continue
    for k in range(3):
      if k == 0:
        dp[i][j][k] += dp[i][j-1][0]
        dp[i][j][k] += dp[i][j-1][2]
      
      if k == 1:
        dp[i][j][k] += dp[i-1][j][1]
        dp[i][j][k] += dp[i-1][j][2]
      
      if k == 2 and arr[i-1][j-2] == 0 and arr[i-2][j-1] == 0:
        dp[i][j][k] += dp[i-1][j-1][0]
        dp[i][j][k] += dp[i-1][j-1][1]
        dp[i][j][k] += dp[i-1][j-1][2]

print(sum(dp[N][N]))