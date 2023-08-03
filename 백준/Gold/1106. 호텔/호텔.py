C, N = map(int, input().split())

dp = [1e9 for _ in range(C+100)]
dp[0] = 0

for _ in range(N):
    cost, people = map(int, input().split())

    for i in range(1, C+100):
        if i - people >= 0:
            dp[i] = min(dp[i], dp[i-people] + cost)
  

print(min(dp[C:]))