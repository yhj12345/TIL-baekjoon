from collections import deque

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs():
    visited = [[[-1, -1] for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 0
    visited[0][0][1] = 0
    q = deque()
    q.append((0, 0, 0))

    while q:
        ti, tj, gram = q.popleft()
        if ti == N-1 and tj == M-1:
            if gram:
                return visited[N-1][M-1][1]
            else:
                return visited[N-1][M-1][0]
        for k in range(4):
            ni = ti + di[k]
            nj = tj + dj[k]

            if 0 > ni or N <= ni or 0 > nj or M <= nj:
                continue

            if gram:
                if visited[ni][nj][1] == -1:
                    if visited[ti][tj][1] == -1:
                        visited[ni][nj][1] = visited[ti][tj][0] + 1
                    else:
                        visited[ni][nj][1] = visited[ti][tj][1] + 1
                    q.append((ni, nj, 1))
            else:
                if visited[ni][nj][0] == -1 and arr[ni][nj] != 1:
                    visited[ni][nj][0] = visited[ti][tj][0] + 1

                    if arr[ni][nj] == 2:
                        q.append((ni, nj, 1))
                    else:
                        q.append((ni, nj, 0))
    return 'Fail'

N, M, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

answer = bfs()
if answer == 'Fail':
    print(answer)
else:
    if answer > T:
        print('Fail')
    else:
        print(answer)