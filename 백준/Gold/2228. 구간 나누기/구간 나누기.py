N, M = map(int, input().split())
arr = list(int(input()) for _ in range(N))
sum_arr = [0 for _ in range(N+1)]

for i in range(1, N+1):
    sum_arr[i] = sum_arr[i-1] + arr[i-1]

dp = [[0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(1, M+1):
    dp[0][i] = -3276800

for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = dp[i-1][j]

        for k in range(1, i+1):
            if k >= 2:
                dp[i][j] = max(dp[i][j], dp[k-2][j-1] + sum_arr[i] - sum_arr[k-1])
            elif k == 1 and j == 1:
                dp[i][j] = max(dp[i][j], sum_arr[i])
print(dp[N][M])