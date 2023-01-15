def solution(info, edges):
  
  def dfs(wolf, sheep, visited, next):
    global answer

    if wolf >= sheep:
      return
    answer = max(answer, sheep)
    for i in next:
      if i not in visited:
        if info[i] == 0:
          dfs(wolf, sheep+1, visited | {i}, next | set(tree[i]))
        else:
          dfs(wolf+1, sheep, visited | {i}, next | set(tree[i]))
  global answer

  answer = 0
  tree = [[] for _ in range(len(info))]
  next_set = set()
  for parent, child in edges:
    tree[parent].append(child)
    if parent == 0:
      next_set.add(child)
  dfs(0, 1, {0}, next_set)
  return answer