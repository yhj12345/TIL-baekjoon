N = int(input())
arr = list(map(int, input().split()))
T = int(input())

sum_arr = [0 for _ in range(N+1)]
for i in range(1, N+1):
    sum_arr[i] = sum_arr[i-1] + arr[i-1]


dp = [[0 for _ in range(N+1)] for _ in range(4)]

for i in range(1, 4):
    for j in range(i * T , N+1):
        if i == 1:
            dp[i][j] = max(dp[i][j-1], sum_arr[j] - sum_arr[j-T])
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j-T] + sum_arr[j] - sum_arr[j-T])

print(dp[3][N])