N, S, M = map(int, input().split())
V = list(map(int, input().split()))
dp = [[False for _ in range(M+1)] for _ in range(N+1)]
dp[0][S] = True

for i in range(N):
    for j in range(M+1):
        if dp[i][j]:
            if j-V[i] >= 0:
                dp[i+1][j-V[i]] = True
            if j+V[i] <= M:
                dp[i+1][j+V[i]] = True

ans = -1
for i in range(M+1):
    if dp[N][i]:
        ans = i

print(ans)