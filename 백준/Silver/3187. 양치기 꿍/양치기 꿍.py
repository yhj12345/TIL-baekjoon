from collections import deque

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    visited[si][sj] = 1

    sheep = 0
    wolf = 0

    if arr[si][sj] == 'k':
        sheep += 1
    elif arr[si][sj] == 'v':
        wolf += 1

    while q:
        ti, tj = q.popleft()

        for k in range(4):
            ni = ti + di[k]
            nj = tj + dj[k]

            if 0 > ni or ni >= R or 0 > nj or nj >= C:
                continue
            
            if visited[ni][nj] == 0 and arr[ni][nj] != '#':
                visited[ni][nj] = 1
                q.append((ni, nj))

                if arr[ni][nj] == 'k':
                    sheep += 1
                elif arr[ni][nj] == 'v':
                    wolf += 1
    return sheep, wolf
  
R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
visited = [[0 for _ in range(C)] for _ in range(R)]
sheep_cnt, wolf_cnt = 0, 0

for i in range(R):
    for j in range(C):
        if visited[i][j] == 0 and arr[i][j] != '#':
            s, w = bfs(i, j)
            if s > w:
                sheep_cnt += s
            else:
                wolf_cnt += w
print(sheep_cnt, wolf_cnt)