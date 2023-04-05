from collections import deque

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(x, y):
    q = deque()
    for i in range(4):
        q.append((x, y, i))
        visited[x][y][i] = 0
    
    while q:
        ti, tj, dir = q.popleft()

        if ti == ei and tj == ej:
            return visited[ti][tj][dir]

        ni = ti + di[dir]
        nj = tj + dj[dir]

        # 다음 좌표가 범위 내이고, 벽이 아닐때
        if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] != '*':
            if visited[ni][nj][dir] == -1 or visited[ni][nj][dir] > visited[ti][tj][dir]:
                visited[ni][nj][dir] = visited[ti][tj][dir]
                q.appendleft((ni, nj, dir))
            
            if arr[ni][nj] == '!':
                if dir == 0 or dir == 2:
                    if visited[ni][nj][1] == -1 or visited[ni][nj][1] > visited[ti][tj][dir] + 1:
                        visited[ni][nj][1] = visited[ti][tj][dir] + 1
                        q.append((ni, nj, 1))
                    if visited[ni][nj][3] == -1 or visited[ni][nj][3] > visited[ti][tj][dir] + 1:
                        visited[ni][nj][3] = visited[ti][tj][dir] + 1
                        q.append((ni, nj, 3))
                elif dir == 1 or dir == 3:
                    if visited[ni][nj][0] == -1 or visited[ni][nj][0] > visited[ti][tj][dir] + 1:
                        visited[ni][nj][0] = visited[ti][tj][dir] + 1
                        q.append((ni, nj, 0))
                    if visited[ni][nj][2] == -1 or visited[ni][nj][2] > visited[ti][tj][dir] + 1:
                        visited[ni][nj][2] = visited[ti][tj][dir] + 1
                        q.append((ni, nj, 2))      
            

n = int(input())
arr = [list(input()) for _ in range(n)]

door = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == '#':
            door.append((i, j))

si, sj, ei, ej = door[0][0], door[0][1], door[1][0], door[1][1]
visited = [[[-1 for _ in range(4)] for _ in range(n)] for _ in range(n)]

result = bfs(si, sj)
print(result)