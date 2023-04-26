N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
dp = [[-1 for _ in range(M)] for _ in range(N)]
arrive = []

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'R':
            dp[i][j] = 0
        elif arr[i][j] == 'O':
            arrive.append((i, j))

di = [-1, 0, 1]
dj = [-1, -1, -1]
for j in range(M):
    for i in range(N):
        if arr[i][j] == '#':
            continue
        
        tmp = []
        for k in range(3):
            ni = i + di[k]
            nj = j + dj[k]

            if 0 > ni or N <= ni or 0 > nj or M <= nj:
                continue
            
            if dp[ni][nj] != -1:
                tmp.append(dp[ni][nj])
            
        if len(tmp) == 0:
            continue
        
        else:
            if arr[i][j] == 'C':
                dp[i][j] = max(tmp) + 1
            else:
                dp[i][j] = max(tmp)
result = []
for x, y in arrive:
    result.append(dp[x][y])

if len(result) == 0:
    print(-1)
elif max(result) == -1:
    print(-1)
else:
    print(max(result))