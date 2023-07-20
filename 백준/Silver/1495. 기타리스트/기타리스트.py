def dfs(depth, vol):
    if visited[depth][vol]:
        return
    
    visited[depth][vol] = True
    
    if depth == N:
        return
    

    
    if vol - V[depth] >= 0:
        dfs(depth+1, vol - V[depth])
    
    if vol + V[depth] <= M:
        dfs(depth+1, vol + V[depth]) 

N, S, M = map(int, input().split())
V = list(map(int, input().split()))
visited = [[False for _ in range(M+1)] for _ in range(N+1)]
ans = -1

dfs(0, S)

for  volume, isPossible in enumerate(visited[N]):
    if isPossible:
        ans = volume

print(ans)