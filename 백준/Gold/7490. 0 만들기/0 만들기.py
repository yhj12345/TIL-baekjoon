def dfs(exp, depth):
  if depth == N:
    tmp = exp.replace(' ', '')
    if eval(tmp) == 0:
      print(exp)
      return
    else:
      return

  dfs(exp+' ' +arr[depth], depth+1)
  dfs(exp+'+'+arr[depth], depth+1)
  dfs(exp+'-'+arr[depth], depth+1)


T = int(input())
for tc in range(T):
  N = int(input())
  arr = [str(i) for i in range(1, N+1)]
  dfs(arr[0], 1)
  if tc != T-1:
    print('')