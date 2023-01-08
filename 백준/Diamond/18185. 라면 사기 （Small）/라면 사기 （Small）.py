import sys

N = int(input())
arr = list(map(int, input().split())) + [0, 0]

result = 0
for i in range(N):
  if arr[i+1] > arr[i+2]:
    a = min(arr[i], arr[i+1] - arr[i+2])
    arr[i] -= a
    arr[i+1] -= a
    result += 5*a

    b = min(arr[i], arr[i+1])
    arr[i] -= b
    arr[i+1] -= b
    arr[i+2] -= b
    result += 7*b
  else:
    a = min(arr[i], arr[i+1])
    arr[i] -= a
    arr[i+1] -= a
    arr[i+2] -= a
    result += 7*a
  result += arr[i] * 3
print(result)