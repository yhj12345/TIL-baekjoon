from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(sx, sy, ex, ey):
    global ans
    visited[sx][sy] = 1
    q = deque()
    q.append((sx, sy))

    while q:
        tx, ty = q.popleft()

        if tx == ex and ty == ey:
            ans = visited[ex][ey] - 1
            return
        
        for k in range(4):
            nx = tx + dx[k]
            ny = ty + dy[k]

            if nx < 0 or nx >= N or ny < 0 or ny >= M or visited[nx][ny] != 0:
                continue
            
            # right
            if k == 0:
                nny = ny + B-1
                for l in range(A):
                    nnx = nx + l

                    if nnx < 0 or nnx >= N or nny < 0 or nny >= M:
                        break
                    if arr[nnx][nny] == 1:
                        break
                    
                else:
                    visited[nx][ny] = visited[tx][ty] + 1
                    q.append((nx, ny))
            
            # down
            elif k == 1:
                nnx = nx + A-1
                for l in range(B):
                    nny = ny + l

                    if nnx < 0 or nnx >= N or nny < 0 or nny >= M:
                        break
                    if arr[nnx][nny] == 1:
                        break
                    
                else:
                    visited[nx][ny] = visited[tx][ty] + 1
                    q.append((nx, ny))
            
            # left
            elif k == 2:
                nny = ny 
                for l in range(A):
                    nnx = nx + l

                    if nnx < 0 or nnx >= N or nny < 0 or nny >= M:
                        break
                    if arr[nnx][nny] == 1:
                        break
                    
                else:
                    visited[nx][ny] = visited[tx][ty] + 1
                    q.append((nx, ny))
            
            # up
            elif k == 3:
                nnx = nx
                for l in range(B):
                    nny = ny + l

                    if nnx < 0 or nnx >= N or nny < 0 or nny >= M:
                        break
                    if arr[nnx][nny] == 1:
                        break
                    
                else:
                    visited[nx][ny] = visited[tx][ty] + 1
                    q.append((nx, ny))

N, M, A, B, K = map(int, input().split())
arr = [[0 for _ in range(M)] for _ in range(N)]

for _ in range(K):
    x, y = map(int, input().split())
    arr[x-1][y-1] = 1

si, sj = map(int, input().split())
ei, ej = map(int, input().split())

visited = [[0 for _ in range(M)] for _ in range(N)]
ans = -1
bfs(si-1, sj-1, ei-1, ej-1)
print(ans)