from collections import deque

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    visited[si][sj] = 1

    while q:
        ti, tj = q.popleft()

        for k in range(4):
            ni = ti + di[k]
            nj = tj + dj[k]

            if 0 > ni or N <= ni or 0 > nj or M <= nj:
                continue
            
            if arr[ni][nj] != 0 and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                q.append((ni, nj))

            elif arr[ni][nj] == 0:
                count[ti][tj] += 1

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

day = 0

while True:
    visited = [[0 for _ in range(M)] for _ in range(N)]
    count = [[0 for _ in range(M)] for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0 and visited[i][j] == 0:
                cnt += 1
                bfs(i, j)

    for i in range(N):
        for j in range(M):
            if count[i][j] != 0:
                arr[i][j] = max(0, arr[i][j] - count[i][j])
    
    if cnt == 0:
        print(0)
        break
    
    if cnt >= 2:
        print(day)
        break
    
    day += 1