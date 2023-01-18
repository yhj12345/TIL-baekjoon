R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

after = []
for i in range(R):
  for j in range(C):
    if arr[i][j] == 'X':
      tmp = 0
      for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] == '.':
          tmp += 1
        elif 0 > ni or ni >= R or 0 > nj or nj >= C:
          tmp += 1
      if tmp >= 3:
        after.append((i, j))
for ti, tj in after:
  arr[ti][tj] = '.'
up_bound, down_bound, left_bound, right_bound = -1, -1, -1, -1
for i in range(R):
  for j in range(C):
    if arr[i][j] == 'X':
      up_bound = i
      break
  if up_bound != -1:
    break
for i in range(C):
  for j in range(R):
    if arr[j][i] == 'X':
      left_bound = i
      break
  if left_bound != -1:
    break
for i in range(R-1, -1, -1):
  for j in range(C-1, -1, -1):
    if arr[i][j] == 'X':
      down_bound = i
      break
  if down_bound != -1:
    break
for i in range(C-1, -1, -1):
  for j in range(R-1, -1, -1):
    if arr[j][i] == 'X':
      right_bound = i
      break
  if right_bound != -1:
    break
result = []
for i in range(up_bound, down_bound+1):
  result.append(arr[i][left_bound: right_bound+1])
for i in range(len(result)):
  print(''.join(result[i]))