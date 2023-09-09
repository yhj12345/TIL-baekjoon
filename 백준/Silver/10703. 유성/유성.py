import sys

R, S = map(int, input().split())
meteor = [input() for _ in range(R)]
arr = [['.'] * S for _ in range(R)]

max_meteor = [-3333] * S
min_ground  = [1 << 14] * S

for i in range(R):
  for j in range(S):
    if meteor[i][j] == 'X':
      max_meteor[j] = max(max_meteor[j], i)
    elif meteor[i][j] == '#':
      min_ground[j] = min(min_ground[j], i)

move = min((j - i for i, j in zip(max_meteor, min_ground))) - 1

for i in range(R):
  for j in range(S):
    if meteor[i][j] == 'X':
      arr[move+i][j] = 'X'
    if meteor[i][j] == '#':
      arr[i][j] = '#'

for i in range(R):
    for j in range(S):
        sys.stdout.write(arr[i][j])
    sys.stdout.write('\n')