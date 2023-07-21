N = int(input())
arr1 = list(map(int, input().split()))
arr2 = arr1[::-1]
dp = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        if arr1[i-1] == arr2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(N-dp[N][N])