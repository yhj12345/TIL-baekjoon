import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

dp = [[False for _ in range(N+1)] for _ in range(N+1)]

for cnt in range(1, N+1):
    for start in range(1, N+1):
        end = start + cnt - 1
        if end >= N + 1:
            break
        
        if cnt == 1:
            dp[start][end] = True
            continue
        
        if cnt == 2:
            if arr[start-1] == arr[end-1]:
                dp[start][end] = True
                continue
        
        if arr[start-1] == arr[end-1] and dp[start+1][end-1]:
            dp[start][end] = True

M = int(input())
for i in range(M):
    S, E = map(int, input().split())
    if dp[S][E]:
        print(1)
    else:
        print(0)