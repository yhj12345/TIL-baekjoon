import sys

def dfs(array, start):
    if len(array) == K:
        for a in array:
            print(a)
        sys.exit()
    
    for i in range(start+1, N+1):
        if visited[i] == 0:
            for num in array:
                if num not in graph[i]:
                    break
            else:
                visited[i] = 1
                dfs(array+[i], i)
      
K, N, F = map(int, input().split())
edges = []
graph = [[] for _ in range(N+1)]
for _ in range(F):
    a, b = map(int, input().split())
    edges.append((a, b))
edges.sort(key = lambda x: (x[0], x[1]))

for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    visited = [0 for _ in range(N+1)]
    visited[i] = 1
    dfs([i], i)

print(-1)