from collections import deque

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(si, sj):
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[si][sj] = 1
    q = deque()
    q.append((si, sj))
    
    while q:
        ti, tj = q.popleft()

        for k in range(4):
            ni = ti + di[k]
            nj = tj + dj[k]

            if 0 > ni or N <= ni or 0 > nj or M <= nj:
                return True
            
            if visited[ni][nj] == 0:
                if arr[ni][nj] == 0:
                    visited[ni][nj] = 1
                    q.append((ni, nj))
    return False

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cheeze = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            cheeze += 1

result = [cheeze]
while cheeze > 0:
    tmp = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                is_melt = bfs(i, j)

                if is_melt:
                    cheeze -=1
                    tmp.append((i, j))
                  
    result.append(cheeze)
    for a, b in tmp:
        arr[a][b] = 0
print(len(result)-1)
print(result[-2])