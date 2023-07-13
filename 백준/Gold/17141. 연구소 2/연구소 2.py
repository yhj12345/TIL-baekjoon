from itertools import combinations
from collections import deque

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(virus_array):
    q = deque()
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for x, y in virus_array:
        q.append((x, y))
        visited[x][y] = 1

    while q:
        ti, tj = q.popleft()
        for k in range(4):
            ni = ti + di[k]
            nj = tj + dj[k]

            if 0 > ni or N <= ni or 0 > nj or N <= nj:
                continue
            
            if visited[ni][nj] == 0 and arr[ni][nj] != 1:
                q.append((ni, nj))
                visited[ni][nj] = visited[ti][tj] + 1
    return visited

def check(array):
    time = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 1:
              if array[i][j] == 0:
                  return -1
              else:
                  time = max(time, array[i][j])
    return time - 1

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

virus = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            virus.append((i, j))

ans = 100000

for combi in combinations(virus, M):
    v = bfs(combi)
    time = check(v)
    if time == -1:
        continue
    else:
        ans = min(ans, time)

if ans == 100000:
    print(-1)
else:
    print(ans)
