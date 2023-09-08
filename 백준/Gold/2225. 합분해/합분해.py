N, K = map(int, input().split())

dp = [[0 for _ in range(N+1)] for _ in range(K+1)]
dp[0][0] = 1

MOD = 1e9

for i in range(1, K+1):
  for j in range(1, N+1):
    for k in range(j+1):
      dp[i][j] += dp[i-1][j-k]
      dp[i][j] %= MOD

ans = 0
for i in dp:
  ans += i[-1]

ans %= MOD
print(int(ans))