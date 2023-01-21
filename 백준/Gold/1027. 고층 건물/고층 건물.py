N = int(input())
arr = list(map(int, input().split()))

result = 0
for i in range(N):
  tmp = 0
  for j in range(i):
    flag = True
    width = i - j             
    if arr[i] > arr[j]:
      height = arr[i] - arr[j] 
      for k in range(j+1, i):
        small_height = ((k-j) * height) / width
        if small_height + arr[j] <= arr[k]:
          flag = False
          break
    elif arr[i] < arr[j]:
      height = arr[j] - arr[i] 
      for k in range(j+1, i):
        small_height = ((i-k) * height) / width
        if small_height + arr[i] <= arr[k]:
          flag = False
          break
    else:
      for k in range(j+1, i):
        if arr[i] <= arr[k]:
          flag = False
          break
    if flag == True:
      tmp += 1
  for j in range(i+1, N):
    flag = True
    width = j - i
    if arr[i] > arr[j]:
      height = arr[i] - arr[j]
      for k in range(i+1, j):
        small_height = ((j-k) * height) / width
        if small_height + arr[j] <= arr[k]:
          flag = False
          break
    elif arr[i] < arr[j]:
      height = arr[j] - arr[i] 
      for k in range(i+1, j):
        small_height = ((k-i) * height) / width
        if small_height + arr[i] <= arr[k]:
          flag = False
          break
    else:
      for k in range(i+1, j):
        if arr[i] <= arr[k]:
          flag = False
          break
    if flag == True:
      tmp += 1
  result = max(result, tmp)   

print(result)