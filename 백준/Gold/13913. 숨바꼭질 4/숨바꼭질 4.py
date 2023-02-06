from collections import deque


def bfs(start):
  visited[start] = -2
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
      visited[c] = now
    if 0 <= b <= 100000 and visited[b] == -1:
      q.append(b)
      visited[b] = now
    if 0 <= a <= 100000 and visited[a] == -1:
      q.append(a)
      visited[a] = now



N, K = map(int, input().split())
visited = [-1 for _ in range(100001)]

result = [K]
bfs(N)
while True:
  a = visited[result[-1]]
  if a == -2:
    break
  result.append(a)
print(len(result)-1)
print(*result[::-1])