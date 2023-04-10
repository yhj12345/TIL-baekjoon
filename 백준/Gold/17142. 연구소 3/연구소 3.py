from collections import deque
from itertools import combinations

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def cal(array):
    time = 0
    for i in range(N):
        for j in range(N):
            if array[i][j] == -1:
                return -1
            
            if time < array[i][j]:
                time = array[i][j]
    return time

def bfs(virus):
    q = deque()
    visited = [[-1 for _ in range(N)] for _ in range(N)]
    for v in virus:
        q.append(v)
        visited[v[0]][v[1]] = 0
    
    while q:
        ti, tj = q.popleft()
        for k in range(4):
            ni = ti + di[k]
            nj = tj + dj[k]
            if 0 > ni or ni >= N or 0 > nj or nj >= N:
                continue
            if arr[ni][nj] == 0 and visited[ni][nj] == -1:
                visited[ni][nj] = visited[ti][tj] + 1
                q.append((ni, nj))
            elif visited[ni][nj] == -1 and arr[ni][nj] == 2:
                q.append((ni, nj))
                visited[ni][nj] = visited[ti][tj] + 1
    return visited

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

virus = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            virus.append((i, j))

ans = 100000
for combi in combinations(virus, M):
    result = bfs(combi)
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                result[i][j] = 0
            elif arr[i][j] == 2:
                result[i][j] = 0
    tmp = cal(result)
    
    if tmp != -1:
        ans = min(ans, tmp)

if ans == 100000:
    print(-1)
else:
    print(ans)