from collections import deque

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def find_island(si, sj, idx):
    q = deque()
    visited[si][sj] = idx
    q.append((si, sj))

    while q:
        ti, tj = q.popleft()
        for k in range(4):
            ni = ti + di[k]
            nj = tj + dj[k]
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = idx

def bridge(idx):
    global answer
    distance = [[-1 for _ in range(N)] for _ in range(N)]
    q = deque()
    for i in range(N):
        for j in range(N):
            if visited[i][j] == idx:
                distance[i][j] = 0
                q.append((i, j))
    
    while q:
        ti, tj = q.popleft()
        for k in range(4):
            ni = ti + di[k]
            nj = tj + dj[k]

            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                continue
            
            if distance[ni][nj] == -1 and visited[ni][nj] == 0:
                distance[ni][nj] = distance[ti][tj] + 1
                q.append((ni, nj))
            
            elif distance[ni][nj] == -1 and visited[ni][nj] >= 1 and visited[ni][nj] != idx:
                answer = min(distance[ti][tj], answer)
                return
                
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]

cnt = 1
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] == 0:
            find_island(i, j, cnt)
            cnt += 1

answer = 10000000

for c in range(1, cnt+1):
    bridge(c)
print(answer)