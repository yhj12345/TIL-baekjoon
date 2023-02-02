N = int(input())
K = int(input())
arr = list(map(int, input().split()))
arr.sort()
start = arr[0]
end = arr[-1]

total = end - start

a = [0 for _ in range(N)]
for i in range(1, N):
  a[i] = arr[i] - arr[i-1]

a.sort()

tmp = 1
while True and a:
  if tmp == K:
    break
  total -= a.pop()
  tmp += 1
print(total)