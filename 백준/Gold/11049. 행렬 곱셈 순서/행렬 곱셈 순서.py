N = int(input())
arr = [list(map(int ,input().split())) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]

for i in range(1, N):
  for j in range(N-i):
    x = i + j
    dp[j][x] = 2 ** 32
    for k in range(j, x):
      dp[j][x] = min(dp[j][x], dp[j][k] + dp[k+1][x] + arr[j][0] * arr[k][1] * arr[x][1])
print(dp[0][N-1])