N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[[0 for _ in range(K+1)] for _ in range(M+1)] for _ in range(N)]

for i in range(N):
    a, b = arr[i]
    for j in range(1, M+1):
        for k in range(1, K+1):
            if j-a >= 0 and k-b >= 0:
                dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j-a][k-b] + 1)
            else:
                dp[i][j][k] = dp[i-1][j][k]
print(dp[N-1][M][K])