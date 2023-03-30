from collections import deque

def solution(maps):
    # bfs
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    def bfs(x, y, ex, ey):
        q = deque()
        visited = [[0 for _ in range(M)] for _ in range(N)]
        visited[x][y] = 1
        q.append((x, y))
        
        while q:
            ti, tj = q.popleft()
            if ti == ex and tj == ey:
                return visited[ti][tj]
            for k in range(4):
                ni = ti + di[k]
                nj = tj + dj[k]
                
                if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and maps[ni][nj] != 'X':
                    q.append((ni, nj))
                    visited[ni][nj] = visited[ti][tj] + 1
        
        return -1
    
    answer = 0
    N = len(maps)
    M = len(maps[0])
    # 시작좌표, 끝좌표, 레버좌표
    si, sj, ei, ej, li, lj = 0, 0, 0, 0, 0, 0
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 'S':
                si, sj = i, j
            elif maps[i][j] == 'L':
                li, lj = i, j
            elif maps[i][j] == 'E':
                ei, ej = i, j
    
    #시작좌표에서 레버좌표로 이동
    start_to_lever = bfs(si, sj, li, lj)
    lever_to_end = bfs(li, lj, ei, ej)
    
    if start_to_lever == -1 or lever_to_end == -1:
        answer = -1
    else:
        answer = start_to_lever - 1 + lever_to_end - 1
    
    
    return answer