from collections import deque

def solution(maps):
    answer = []
    
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    
    def bfs(si, sj):
        q = deque()
        cost = int(maps[si][sj])
        visited[si][sj] = 1
        q.append((si, sj))
        
        while q:
            ti, tj = q.popleft()
            for k in range(4):
                ni = ti + di[k]
                nj = tj + dj[k]
                
                if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] == 0 and maps[ni][nj] != 'X':
                    cost += int(maps[ni][nj])
                    visited[ni][nj] = 1
                    q.append((ni, nj))
        return cost
        
        
    n = len(maps)
    m = len(maps[0])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and maps[i][j] != 'X':
                result = bfs(i, j)
                answer.append(result)
    if len(answer) == 0:
        answer.append(-1)
    else:
        answer.sort()
    return answer