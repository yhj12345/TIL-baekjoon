import sys
sys.setrecursionlimit(10 ** 5)

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def dfs(si, sj):
    if dp[si][sj]:
        return dp[si][sj]
    
    dp[si][sj] = 1

    for k in range(4):
        ni = si + di[k]
        nj = sj + dj[k]

        if 0 > ni or n <= ni or 0 > nj or n <= nj:
            continue
        
        if arr[si][sj] < arr[ni][nj]:
            dp[si][sj] = max(dp[si][sj], dfs(ni, nj)+1)
    
    return dp[si][sj]

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, dfs(i, j))

print(ans)