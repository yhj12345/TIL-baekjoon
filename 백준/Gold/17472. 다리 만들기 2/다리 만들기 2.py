from collections import deque


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def find_island(si, sj):
    island = [(si, sj)]

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

            if visited[ni][nj] == 0 and arr[ni][nj] == 1:
                q.append((ni, nj))
                island.append((ni, nj))
                visited[ni][nj] = 1
    return island

def connect_bridge(island, idx):
    q = deque()

    for a, b in island:
        q.append((a, b, 0, 0))
        q.append((a, b, 1, 0))
        q.append((a, b, 2, 0))
        q.append((a, b, 3, 0))
    
    while q:
        ti, tj, d, cnt = q.popleft()

        ni = ti + di[d]
        nj = tj + dj[d]

        if 0 > ni or N <= ni or 0 > nj or M <= nj:
                continue
        
        if new_arr[ni][nj] != 0 and new_arr[ni][nj] != idx and cnt > 1:
            if (cnt, idx, new_arr[ni][nj]) not in edges:
                edges.append((cnt, idx, new_arr[ni][nj]))
        
        elif new_arr[ni][nj] == 0:
            q.append((ni, nj, d, cnt+1))

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parents[y] = x
    else:
        parents[x] = y

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

island_list = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and visited[i][j] == 0:
            island = find_island(i, j)
            island_list.append(island)

new_arr = [[0 for _ in range(M)] for _ in range(N)]
for i in range(len(island_list)):
    for a, b in island_list[i]:
        new_arr[a][b] = i+1

edges = []
parents = [i for i in range(len(island_list)+1)]
for i in range(len(island_list)):
    connect_bridge(island_list[i], i+1)

edges.sort(key=lambda x: (x[0], x[1], x[2]))
ans = 0
tmp = 0
for dist, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        ans += dist
        tmp += 1
if tmp + 1 == len(island_list):
    print(ans)
else:
    print(-1)