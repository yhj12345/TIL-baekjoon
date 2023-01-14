import sys
sys.setrecursionlimit(100000)


def binary_search(s, e):
  global result
  if s > e:
    return
  mid = (s + e) // 2
  cnt = 1
  tmp = mid
  for i in range(N):
    if tmp < arr[i]:
      tmp = mid
      cnt += 1
    tmp -= arr[i]
  if cnt > M or mid < max(arr):
    binary_search(mid+1, e)
  else:
    result = min(mid, result)
    binary_search(s, mid-1)

N, M = map(int, input().split())
arr = list(int(input()) for _ in range(N))
start = min(arr)
end = sum(arr)
result = sum(arr)
binary_search(start, end)
print(result)