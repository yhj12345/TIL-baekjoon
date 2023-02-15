from collections import deque

N = int(input())
arr = list(input().split())
arr.sort()
parent_dict = dict()
child = dict()

for i in range(N):
  parent_dict[arr[i]] = []
  child[arr[i]] = []
M = int(input())

for _ in range(M):
  a, b = input().split()
  parent_dict[a].append(b)

result = deque()
grand_parent = []
visited = set()
for parent in parent_dict:
  if len(parent_dict[parent]) == 0:
    result.append(parent)
    grand_parent.append(parent)
    visited.add(parent)
grand_parent.sort()
print(len(grand_parent))
print(*grand_parent)
cnt = len(result)

while result:
  tmp = result.popleft()
  for parent in parent_dict:
    if tmp in parent_dict[parent]:
      parent_dict[parent].pop(parent_dict[parent].index(tmp))

    if len(parent_dict[parent]) == 0 and parent not in visited:
      child[tmp].append(parent)
      result.append(parent)
      visited.add(parent)

for i in arr:
  k = child[i]
  k.sort()
  print(i, end=' ')
  print(len(k), end=' ')
  print(*k)