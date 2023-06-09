from collections import deque

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(si, sj):
    q = deque()
    for i in range(4):
        mirror[si][sj][i] = 0
        q.append((si, sj, i, 0))
    
    while q:
        ti, tj, d, m = q.popleft()
        ni = ti + di[d]
        nj = tj + dj[d]

        left = (d + 1) % 4
        right = (d - 1) % 4

        if 0 > ni or ni >= H or 0 > nj or nj >= W:
            continue
        
        if arr[ni][nj] == '*':
            continue
        
        if mirror[ni][nj][d] == -1:
            mirror[ni][nj][d] = m
            q.append((ni, nj, d, m))
            q.append((ni, nj, left, m+1))
            q.append((ni, nj, right, m+1))

        else:
            if mirror[ni][nj][d] > m:
                mirror[ni][nj][d] = m
                q.append((ni, nj, d, m))
                q.append((ni, nj, left, m+1))
                q.append((ni, nj, right, m+1))
          

W, H = map(int, input().split())
arr = [list(input()) for _ in range(H)]
mirror = [[[-1 for _ in range(4)] for _ in range(W)] for _ in range(H)]
target = []
for i in range(H):
    for j in range(W):
        if arr[i][j] == 'C':
            target.append((i, j))
si, sj = target[0]
ei, ej = target[1]

bfs(si, sj)

result = []
for m in mirror[ei][ej]:
    if m != -1:
        result.append(m)
print(min(result))