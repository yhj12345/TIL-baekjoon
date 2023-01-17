import sys

N = int(input())
dp = [[0 for _ in range(6)] for _ in range(N+1)]
dp[0][0] = 1

for i in range(1, N+1):
  dp[i][0] = dp[i-1][0] + dp[i-1][1] + dp[i-1][2]
  dp[i][1] = dp[i-1][0]
  dp[i][2] = dp[i-1][1]
  dp[i][3] = dp[i-1][0] + dp[i-1][1] + dp[i-1][2] + dp[i-1][3] + dp[i-1][4] + dp[i-1][5] 
  dp[i][4] = dp[i-1][3]
  dp[i][5] = dp[i-1][4]
print(sum(dp[N]) % 1000000)