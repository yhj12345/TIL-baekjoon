N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[[1000000 for _ in range(3)] for _ in range(M)] for _ in range(N)]
d = [-1, 0, 1]
for i in range(M):
    for j in range(3):
        dp[0][i][j] = arr[0][i]

for i in range(1, N):
    for j in range(M):
        for k in range(3):
            ny = j + d[k]
            if 0 <= ny < M:              
                for l in range(3):
                    if l != k:
                        dp[i][j][k] = min(dp[i][j][k], dp[i-1][ny][l] + arr[i][j])
ans = 10000000
for i in range(M):
    for k in range(3):
        ans = min(ans, dp[N-1][i][k])
print(ans)