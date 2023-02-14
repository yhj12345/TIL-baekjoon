import sys

def bfs(si, sj):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    fish_info = []
    q = []
    q.append((si, sj))
    visited[si][sj] = 1

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    while q:
        ti, tj = q.pop(0)

        for k in range(4):
            ni = ti + di[k]
            nj = tj + dj[k]

            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                if arr[ni][nj] <= shark_size:
                    q.append((ni, nj))
                    visited[ni][nj] = visited[ti][tj] + 1
                    if 0 < arr[ni][nj] < shark_size:
                        fish_info.append((ni, nj, visited[ni][nj]-1))
    return sorted(fish_info, key=lambda x: (x[2], x[0], x[1]))


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
shark_size = 2
fish_cnt = 0

for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            shark_x = i
            shark_y = j
            arr[i][j] = 0
        elif 0 < arr[i][j] <= 6:
            fish_cnt += 1


result = 0
eat_fish = 0
while fish_cnt:
    temp = bfs(shark_x, shark_y)
    if not temp:
        break
    near_fish = temp[0]
    shark_x, shark_y = near_fish[0], near_fish[1]
    result += near_fish[2]
    arr[shark_x][shark_y] = 0
    fish_cnt -= 1
    eat_fish += 1

    if eat_fish == shark_size:
        shark_size += 1
        eat_fish = 0
print(result)