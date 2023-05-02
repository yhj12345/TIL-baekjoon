dir_dict = {0: [(0, -1), (1, 0)], 1: [(-1, 0), (0, -1)], 2: [(-1, 0), (0, 1)], 3: [(1, 0), (0, 1)]}

def dfs(x, y, cnt):
    global ans
    if y == M:
        x += 1
        y = 0

    if x == N:
        ans = max(ans, cnt)
        return
    
    if visited[x][y] == 0:
        for d in dir_dict:
            nx1 = x + dir_dict[d][0][0]
            ny1 = y + dir_dict[d][0][1]

            nx2 = x + dir_dict[d][1][0]
            ny2 = y + dir_dict[d][1][1]

            if 0 > nx1 or N <= nx1 or 0 > ny1 or M <= ny1 or 0 > nx2 or N <= nx2 or 0 > ny2 or M <= ny2:
                continue

            if visited[nx1][ny1] == 0 and visited[nx2][ny2] == 0:
                visited[x][y] = 1
                visited[nx1][ny1] = 1
                visited[nx2][ny2] = 1
                dfs(x, y+1, cnt + 2 * arr[x][y] + arr[nx1][ny1] + arr[nx2][ny2])
                visited[x][y] = 0
                visited[nx1][ny1] = 0
                visited[nx2][ny2] = 0
    
    dfs(x, y+1, cnt)

        

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
ans = 0
dfs(0, 0, 0)
print(ans)