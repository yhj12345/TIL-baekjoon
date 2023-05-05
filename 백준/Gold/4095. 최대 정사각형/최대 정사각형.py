while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
    ans = 0

    for i in range(1, N+1):
        for j in range(1, M+1):
            if arr[i-1][j-1] == 0:
                continue
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
            ans = max(dp[i][j], ans)
    print(ans)