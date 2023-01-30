from itertools import combinations

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def check(ti, tj, dir, bar):
  while True:
    ti = ti + di[dir]
    tj = tj + dj[dir]

    if 0 <= ti < N and 0 <= tj < N:
      if (ti, tj) in bar:
        return 1
      elif arr[ti][tj] == 'S':
        return 0
    else:
      return 1

N = int(input())
arr = [list(input().split()) for _ in range(N)]

teacher = []
student = []
barrier = []
for i in range(N):
  for j in range(N):
    if arr[i][j] == 'T':
      teacher.append((i, j))
    elif arr[i][j] == 'S':
      student.append((i, j))
    else:
      barrier.append((i, j))


flag = False
for combi in combinations(barrier, 3):
  cnt1 = 0
  for tx, ty in teacher:
    cnt2 = 0
    for k in range(4):
      ret = check(tx, ty, k, combi)
      cnt2 += ret
    if cnt2 == 4:
      cnt1 += 1
  if cnt1 == len(teacher):
    print('YES')
    flag = True
    break
        
if flag == False:
  print('NO')