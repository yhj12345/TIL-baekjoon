from collections import deque

def solution(land, height):
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    
    def bfs(si, sj, cnt):
        q = deque()
        visited[si][sj] = cnt
        q.append((si, sj))
        
        while q:
            ti, tj = q.popleft()
            for k in range(4):
                ni = ti + di[k]
                nj = tj + dj[k]
            
                if 0 > ni or N <= ni or 0 > nj or N <= nj:
                    continue

                if visited[ni][nj] == 0 and abs(land[ni][nj] - land[ti][tj]) <= height:
                    q.append((ni, nj))
                    visited[ni][nj] = cnt
    
    def find_ladder(si, sj):
        for k in range(4):
            ni = si + di[k]
            nj = sj + dj[k]

            if 0 > ni or N <= ni or 0 > nj or N <= nj:
                continue
            
            if visited[si][sj] != visited[ni][nj]:
                edges.append((abs(land[ni][nj] - land[si][sj]), visited[si][sj], visited[ni][nj]))
    
    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        x = find(x)
        y = find(y)
        
        if x < y:
            parent[y] = x
        else:
            parent[x] = y
            
    answer = 0
    N = len(land)
    visited = [[0 for _ in range(N)] for _ in range(N)]
    cnt = 1
    
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                bfs(i, j, cnt)
                cnt += 1
    
    edges = []
    for i in range(N):
        for j in range(N):
            find_ladder(i, j)
    edges.sort()
    parent = [i for i in range(cnt)]
    
    for h, x, y in edges:
        if find(x) != find(y):
            union(x, y)
            answer += h
        
    return answer