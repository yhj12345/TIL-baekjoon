N, M = map(int, input().split())
arr = list(map(int, input().split()))
if N <= M:
  print(N)
else:
  start = 0
  end = 60000000000
  result = (start + end) // 2
  while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for time in arr:
      cnt += (mid // time) + 1
    
    if N <= cnt:
      result = mid
      end = mid - 1
    else:
      start = mid + 1
  cnt = M    
  for time in arr:
    cnt += (result-1) // time
  
  for i in range(M):
    if result % arr[i] == 0:
      cnt += 1
    if cnt == N:
      print(i+1)
      break
