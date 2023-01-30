from collections import deque
N = int(input())
K = int(input())
apple = [list(map(int, input().split())) for _ in range(K)]
L = int(input())
direction = [list(input().split()) for _ in range(L)]

arr = [[0 for _ in range(N)] for _ in range(N)]
for x, y in apple:
  arr[x-1][y-1] = 1

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# 시작 좌표
sx, sy = 0, 0
# 현재시간, 현재 가능 방향
now, now_dir = 0, 0
# 방향 바꾸는 시간, 바뀌는 방향
time, dir = direction.pop(0)

snake = deque()
snake.append((0, 0))
while True:
  nx = sx + di[now_dir]
  ny = sy + dj[now_dir]
  now += 1
  if now == int(time):
    if dir == "L":
      now_dir = (now_dir-1) % 4
    else:
      now_dir = (now_dir+1) % 4
    if len(direction) > 0:
      time, dir = direction.pop(0)
  
  if 0 <= nx < N and 0 <= ny < N:
    if (nx, ny) in snake:
      break
    snake.append((nx, ny))
    sx, sy = nx, ny
    if arr[nx][ny] != 1:
      snake.popleft()
    else:
      arr[nx][ny] = 0
  else:
    break
print(now)