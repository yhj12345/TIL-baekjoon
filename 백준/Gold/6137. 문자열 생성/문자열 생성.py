from collections import deque

N = int(input())
arr = deque()
for i in range(N):
  arr.append(input())

result = []
while len(arr) >= 2:
  if arr[0] < arr[-1]:
    result.append(arr.popleft())
  elif arr[0] > arr[-1]:
    result.append(arr.pop())
  else:
    flag = True
    for i in range(1, len(arr)//2):
      if arr[i] > arr[len(arr)-i-1]:
        break
      elif arr[i] < arr[len(arr)-i-1]:
        flag = False
        break
    if flag:
      result.append(arr.pop())
    else:
      result.append(arr.popleft())
result.append(arr.pop())

tmp = 0
for i in result:
  if tmp == 80:
    print()
    tmp = 0
  print(i, end="")
  tmp += 1