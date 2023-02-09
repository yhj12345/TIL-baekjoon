N, M = map(int, input().split())
A = list(map(int, input().split()))

start = 0
end = 10 ** 12
ans = 10 ** 6
while start <= end:
  mid = (start+end) // 2
  cnt = 0
  for i in A:
    cnt += mid // i
  
  if cnt >= M:
    ans = mid
    end = mid-1
  else:
    start = mid + 1
print(ans)