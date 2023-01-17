import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


def dfs(start, cnt):
  global result
  flag = False
  visited[start] = 1
  for next in graph[start]:
    if visited[next] == 0:
      flag = True
      break
  if flag == False:
    result += cnt
    return
  
  for next in graph[start]:
    if visited[next] == 0:
      visited[next] = 1
      dfs(next, cnt+1)


N = int(input())
graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
result = 0
for _ in range(N-1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
dfs(1, 0)

if result % 2 == 0:
  print('No')
else:
  print('Yes')