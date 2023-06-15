from collections import deque

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(rx, ry, bx, by):
    q = deque()
    visited[rx][ry][bx][by] = 1
    q.append((rx, ry, bx, by))

    while q:
        ri, rj, bi, bj = q.popleft()

        for k in range(4):
            tri, trj, tbi, tbj = ri, rj, bi, bj
            arr[ri][rj] = 'R'
            arr[bi][bj] = 'B'
            flag = False
            isRedGoal = False
            isBlueGoal = False
            while True:
                nri = tri + di[k]
                nrj = trj + dj[k]
                if arr[nri][nrj] == '#':
                    break
                elif arr[nri][nrj] == 'B':
                    arr[tri][trj] = '.'
                    flag = True
                    break
                elif arr[nri][nrj] == '.':
                    arr[tri][trj] = '.'
                    arr[nri][nrj] = 'R'
                    tri, trj = nri, nrj
                elif arr[nri][nrj] == 'O':
                    arr[tri][trj] = '.'
                    isRedGoal = True
                    break

            while True:    
                nbi = tbi + di[k]
                nbj = tbj + dj[k]

                if arr[nbi][nbj] == '#' or arr[nbi][nbj] == 'R':
                    break
                elif arr[nbi][nbj] == '.':
                    arr[tbi][tbj] = '.'
                    arr[nbi][nbj] = 'B'
                    tbi, tbj = nbi, nbj
                elif arr[nbi][nbj] == 'O':
                    isBlueGoal = True
                    break
                
            if flag:
                d = (k-2) % 4
                tri = tbi + di[d]
                trj = tbj + dj[d]

            if isRedGoal and not isBlueGoal:
                return visited[ri][rj][bi][bj]
            
            elif not isRedGoal and not isBlueGoal and visited[tri][trj][tbi][tbj] == 0:
                visited[tri][trj][tbi][tbj] = visited[ri][rj][bi][bj] + 1
                q.append((tri, trj, tbi, tbj))
            arr[tri][trj] = '.'
            arr[tbi][tbj] = '.'
        
    return -1


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
visited = [[[[0 for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)]

ri, rj , bi, bj = 0, 0, 0, 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'R':
            ri, rj = i, j
            arr[i][j] = '.'
        elif arr[i][j] == 'B':
            bi, bj = i, j
            arr[i][j] = '.'
result = bfs(ri, rj, bi, bj)
print(result)