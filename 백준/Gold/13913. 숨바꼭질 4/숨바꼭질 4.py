from collections import deque


def bfs(start):
  visited[start] = 0
  q = deque()
  q.append(start)

  while q:
    now = q.popleft()
    if now == K:
      return

    a = 2 * now
    b = now + 1
    c = now -1
    if 0 <= c <= 100000 and visited[c] == -1:
      q.append(c)
      visited[c] = visited[now] + 1
      route[c] = now
    if 0 <= b <= 100000 and visited[b] == -1:
      q.append(b)
      visited[b] = visited[now] + 1
      route[b] = now
    if 0 <= a <= 100000 and visited[a] == -1:
      q.append(a)
      visited[a] = visited[now] + 1
      route[a] = now



N, K = map(int, input().split())
visited = [-1 for _ in range(100001)]
route = [-1]*100001

result = [K]
bfs(N)
dist = visited[K]
print(dist)
for i in range(dist):
  result.append(route[result[-1]])
print(*result[::-1], end=' ')