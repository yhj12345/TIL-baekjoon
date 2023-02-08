import sys
sys.setrecursionlimit(10 ** 5)

def dfs(start):
  visited[start] = 1
  tmp = []
  for node in graph[start]:
    if visited[node] == 0:
      tmp.append(node)
      dfs(node)
  dp[start][1] = population[start-1]
  for i in range(len(tmp)):
    dp[start][0] += max(dp[tmp[i]])
    dp[start][1] += dp[tmp[i]][0]


N = int(input())
population = list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
dp = [[0, 0] for _ in range(N+1)]

for _ in range(N-1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
dfs(1)
print(max(dp[1]))