N = int(input())
arr = list(map(int, input().split()))
arr.sort()

ans = 1

for x in range(N-1):
  for y in range(N-1, -1, -1):
    if y < x+1:
      continue

    if arr[x] + arr[x+1] > arr[y]:
      ans = max(y-x+1, ans)

print(ans)