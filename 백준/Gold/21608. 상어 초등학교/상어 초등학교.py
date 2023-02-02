import sys
input = sys.stdin.readline
n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)] 

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

like_dict = dict()
for s in range(n**2):
  a, b, c, d, e = map(int, input().split())
  like = {b, c, d, e}
  like_dict[a] = like
  where = []
  for i in range(n):
    for j in range(n):
      if arr[i][j] == 0:
        like_cnt = 0
        empty_cnt = 0
        for k in range(4):
          ni = i + di[k]
          nj = j + dj[k]
          if 0 <= ni < n and 0 <= nj < n:
            if arr[ni][nj] in like:
              like_cnt += 1
            elif arr[ni][nj] == 0:
              empty_cnt += 1
        where.append([like_cnt, empty_cnt, i, j])
  where.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
  li, emp, ti, tj = where[0]
  arr[ti][tj] = a
ans = 0
for i in range(n):
  for j in range(n):
    like = like_dict[arr[i][j]]
    like_cnt = 0
    for k in range(4):
      ni = i + di[k]
      nj = j + dj[k]
      if 0 <= ni < n and 0 <= nj < n:
        if arr[ni][nj] in like:
          like_cnt += 1
    if like_cnt != 0:
      ans += 10 ** (like_cnt-1)
print(ans)