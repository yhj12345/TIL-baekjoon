d = [(-1, 0), (0, 1), (1, 0), (0, -1)]

N, M = map(int, input().split())
sx, sy, dir = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0
while True:
  if arr[sx][sy] == 0:
    arr[sx][sy] = 2
    ans += 1
  
  before_clean_cnt = 0
  for k in range(4):
    nx = sx + d[k][0]
    ny = sy + d[k][1]
    if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0:
      before_clean_cnt += 1
  
  if before_clean_cnt:
    dir = (dir - 1) % 4
    nx = sx + d[dir][0]
    ny = sy + d[dir][1]

    if 0 <= nx < N and 0 <= ny < M:
      if arr[nx][ny] == 0:
        sx += d[dir][0]
        sy += d[dir][1]

  else:
    nx = sx + d[(dir+2) % 4][0]
    ny = sy + d[(dir+2) % 4][1]
    if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] != 1:
      sx += d[(dir+2) % 4][0]
      sy += d[(dir+2) % 4][1]
    else:
      break

print(ans)