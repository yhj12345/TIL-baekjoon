def dfs(array, depth, idx):
  if depth == M:
    print(*array)
    return
  for i in range(idx, len(arr)):
    dfs(array+[arr[i]], depth+1, i)

N, M = map(int, input().split())
arr = list(set(map(int, input().split())))
arr.sort()
dfs([], 0, 0)