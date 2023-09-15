def check():
  for start in range(1, N+1):
    now = start
    for j in range(1, H+1):
      if arr[j][now]:
        now += 1
      elif now > 0 and arr[j][now-1]:
        now -= 1

    if now != start:
      return False
    
  return True

def dfs(cnt, x, y):
  global ans
  if check():
    ans = min(ans, cnt)
    return
  
  elif cnt == 3 or ans <= cnt:
    return
  
  for i in range(x, H+1):
    if i == x:
      now = y
    else:
      now = 0
    
    for j in range(now, N):
      if not arr[i][j] and not arr[i][j+1]:
        if j > 0 and arr[i][j-1]:
          continue

        arr[i][j] = True
        dfs(cnt+1, i, j+2)
        arr[i][j] = False


N, M, H = map(int, input().split())

arr = [[False] * (N+1) for _ in range(H+1)]

for _ in range(M):
  a, b = map(int, input().split())
  arr[a][b] = True

ans = 4
dfs(0, 1, 1)
print(ans if ans < 4 else -1)