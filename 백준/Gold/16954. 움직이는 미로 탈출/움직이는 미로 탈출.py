from collections import deque

di = [0, 0, 1, 0, -1, -1, 1, 1, -1]
dj = [0, 1, 0, -1, 0, 1, 1, -1, -1]

def move_wall(walls):
    new_walls = []
    for x, y in walls:
        if x + 1 < 8:
            new_walls.append((x+1, y))
    
    return new_walls

def bfs():
   global ans
   q = deque()
   q.append((7, 0, walls, 0))

   while q:
      ti, tj, now_walls, time = q.popleft()
      next_walls = move_wall(now_walls)

      if ti == 0 and tj == 7:
          ans = 1
          return

      if time >= 8:
          time = 7
      
      for k in range(9):
          ni = ti + di[k]
          nj = tj + dj[k]

          if 0 > ni or ni >= 8 or 0 > nj or nj >= 8:
              continue
          
          flag = False
          
          for a, b in now_walls:
              if a == ni and b == nj:
                  flag = True
                  break
          
          for a, b in next_walls:
              if a == ni and b == nj:
                  flag = True
                  break
          
          if flag:
              continue
          
          if visited[time][ni][nj] == True:
              continue
          
          q.append((ni, nj, next_walls, time+1))
          visited[time][ni][nj] = True
                 
        



arr = [list(input()) for _ in range(8)]
visited = [[[False for _ in range(8)] for _ in range(8)] for _ in range(8)]

walls = []
for i in range(8):
   for j in range(8):
      if arr[i][j] == '#':
          walls.append((i, j))

ans = 0
bfs()
print(ans)