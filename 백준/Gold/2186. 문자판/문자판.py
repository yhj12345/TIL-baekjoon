import sys

di = [0, -1, 0, 1]
dj = [1, 0, -1, 0]



def dfs(x, y, idx):
    if idx == len(word):
        return 1
    if visited[x][y][idx] != -1:
        return visited[x][y][idx]

    visited[x][y][idx] = 0
    for i in range(4):
        temp_x, temp_y = x, y
        for _ in range(K):
            nx = temp_x + di[i]
            ny = temp_y + dj[i]
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == word[idx]:
                    visited[x][y][idx] += dfs(nx, ny, idx+1)
            temp_x, temp_y = nx, ny
    return visited[x][y][idx]

N, M, K = map(int, input().split())
arr = [list(input()) for _ in range(N)]
word = input()

start = []
end = []
for i in range(N):
  for j in range(M):
    if arr[i][j] == word[0]:
      start.append((i, j))

answer = 0
visited = [[[-1 for _ in range(len(word))] for _ in range(M)] for _ in range(N)]
for si, sj in start:
  answer += dfs(si, sj, 1)
print(answer)