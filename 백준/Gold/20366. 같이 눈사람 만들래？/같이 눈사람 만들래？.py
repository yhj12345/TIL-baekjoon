N = int(input())
H = list(map(int, input().split()))
H.sort()
arr = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
  for j in range(i+1,N):
    arr[i][j] = H[i] + H[j]


answer = 1000000000000000
for i in range(N-3):
  for j in range(3+i, N):
    tmp = arr[i][j]
    start = i + 1
    end = j - 1
    while start < end:
      now = arr[start][end]
      answer = min(abs(tmp - now), answer)
      if now < tmp:
        start += 1
      elif now > tmp:
        end -= 1
      else:
        break
    if answer == 0:
      break
  if answer == 0:
    break
print(answer)