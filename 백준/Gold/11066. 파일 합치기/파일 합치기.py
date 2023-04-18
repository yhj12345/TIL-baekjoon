T = int(input())
for tc in range(T):
    K = int(input())
    arr = list(map(int, input().split()))
    dp = [[0 for _ in range(K+1)] for _ in range(K+1)]
    S = [0 for _ in range(K+1)]

    for i in range(1, K+1):
        S[i] = S[i-1] + arr[i-1]
    
    for i in range(1, K):
        for j in range(K, i, -1):
            dp[j-i][j] = min([dp[j-i][j-i+k] + dp[j-(i-k-1)][j] for k in range(i)]) + (S[j]- S[j-i-1])
    
    print(dp[1][K])