N = int(input())
arr = list(map(int, input().split()))

dp = [0 for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(i):
        temp = arr[j:i]
        dp[i] = max(dp[i], dp[j] + abs(max(temp) - min(temp)))
print(dp[N])