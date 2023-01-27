def mine(array, index):
  array[index-1] += 1
  array[index] += 1
  if index+1 < len(array):
    array[index+1] += 1


T = int(input())
for tc in range(T):
  N = int(input())
  mine_num = list(map(int, input()))
  mine_info = list(input())

  ans = -1
  # 0번이 뭔지모를 때
  if mine_info[0] == '#':
    # 0번에 지뢰가 없다고 가정하고 구함
    result1 = 0
    arr = [0 for _ in range(N)]
    for i in range(1, N):
      if mine_info[i] == '*':
        mine(arr, i)
        result1 += 1
      elif mine_info[i] == '#':
        if arr[i-1] + 1 > mine_num[i-1]:
          continue
        else:
          mine(arr, i)
          result1 += 1
    if arr == mine_num:
      ans = result1
    # 0번에 지뢰가 있다고 가정하고 구함
    result2 = 1
    arr = [0 for _ in range(N)]
    arr[0], arr[1] = 1, 1
    for i in range(1, N):
      if mine_info[i] == '*':
        mine(arr, i)
        result2 += 1
      elif mine_info[i] == '#':
        if arr[i-1] + 1 > mine_num[i-1]:
          continue
        else:
          mine(arr, i)
          result2 += 1
    if arr == mine_num:
      ans = max(ans, result2)
  else:
    result = 1
    arr = [0 for _ in range(N)]
    arr[0], arr[1] = 1, 1
    for i in range(1, N):
      if mine_info[i] == '*':
        mine(arr, i)
        result += 1
      elif mine_info[i] == '#':
        if arr[i-1] + 1 > mine_num[i-1]:
          continue
        else:
          mine(arr, i)
          result += 1
    if arr == mine_num:
      ans = result2
  print(ans)