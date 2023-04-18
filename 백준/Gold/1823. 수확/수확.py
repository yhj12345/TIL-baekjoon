import sys
sys.setrecursionlimit(10 ** 5)
def dfs(s, e):
    if s > e:
        return 0
    
    if dp[s][e] != 0:
        return dp[s][e]
    
    time = N - (e - s)
    dp[s][e] = max(dfs(s+1, e) + arr[s-1] * time, dfs(s, e-1) + arr[e-1] * time)

    return dp[s][e]

N = int(input())
arr = [int(input()) for _ in range(N)]
dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
print(dfs(1, N))