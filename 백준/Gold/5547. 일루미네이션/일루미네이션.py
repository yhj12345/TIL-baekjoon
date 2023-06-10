from collections import deque

def bfs(si, sj):
    flag = True
    q = deque()
    visited[si][sj] = 1
    check = [(si, sj)]
    q.append((si, sj))

    while q:
        ti, tj = q.popleft()

        if ti % 2 == 0:
            di = even_di
            dj = even_dj
        else:
            di = odd_di
            dj = odd_dj
        
        for k in range(6):
            ni = ti + di[k]
            nj = tj + dj[k]

            if 0 > ni or ni >= H or 0 > nj or nj >= W:
                flag = False
                continue
            
            if visited[ni][nj] == 0 and arr[ni][nj] == 0:
                q.append((ni, nj))
                check.append((ni, nj))
                visited[ni][nj] = 1
    if flag:
        for a, b in check:
            arr[a][b] = 1



W, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(H)]

odd_di = [-1, -1, 0, 0, 1, 1]
odd_dj = [-1, 0, 1, -1, -1, 0]

even_di = [-1, -1, 0, 1, 1, 0]
even_dj = [0, 1, 1, 1, 0, -1]
visited = [[0 for _ in range(W)] for _ in range(H)]

for i in range(H):
    for j in range(W):
        if arr[i][j] == 0 and visited[i][j] == 0:
            bfs(i, j)

answer = 0
for i in range(H):
    for j in range(W):
        if i % 2 == 0:
            di = even_di
            dj = even_dj
        else:
            di = odd_di
            dj = odd_dj
        if arr[i][j] == 1:
            tmp = 0

            for k in range(6):
                ni = i + di[k]
                nj = j + dj[k]

                if 0 > ni or ni >= H or 0 > nj or nj >= W:
                    tmp += 1
                    continue
                
                if arr[ni][nj] == 0:
                    tmp +=1

            answer += tmp

print(answer)