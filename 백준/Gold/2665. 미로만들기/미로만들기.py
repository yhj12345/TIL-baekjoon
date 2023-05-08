from collections import deque

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    visited[si][sj] = 0

    while q:
        ti, tj = q.popleft()

        for k in range(4):
            ni = ti + di[k]
            nj = tj + dj[k]

            if 0 > ni or n <= ni or 0 > nj or n <= nj:
                continue
            
            if arr[ni][nj] == '1':
                if visited[ni][nj] == -1:
                    q.append((ni, nj))
                    visited[ni][nj] = visited[ti][tj]

                elif visited[ti][tj] < visited[ni][nj]:
                    q.append((ni, nj))
                    visited[ni][nj] = visited[ti][tj]
            
            elif arr[ni][nj] == '0':
                if visited[ni][nj] == -1:
                    q.append((ni, nj))
                    visited[ni][nj] = visited[ti][tj] + 1
                    
                elif visited[ti][tj] + 1 < visited[ni][nj]:
                    q.append((ni, nj))
                    visited[ni][nj] = visited[ti][tj] + 1

n = int(input())
arr = [list(input()) for _ in range(n)]
visited = [[-1 for _ in range(n)] for _ in range(n)]

bfs(0, 0)
print(visited[n-1][n-1])
