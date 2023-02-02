n = int(input())
start = list(map(int, input().split()))
dp = [[0, 0], [0, 0], [0, 0]]

for i in range(3):
  for j in range(2):
    dp[i][j] = start[i]

for i in range(n-1):
  next = list(map(int, input().split()))
  a = next[0] + max(dp[0][0], dp[1][0])
  aa = next[0] + min(dp[0][1], dp[1][1])
  b = next[1] + max(dp[0][0], dp[1][0], dp[2][0])
  bb = next[1] + min(dp[0][1], dp[1][1], dp[2][1])
  c = next[2] + max(dp[1][0], dp[2][0])
  cc = next[2] + min(dp[1][1], dp[2][1])
  dp[0], dp[1], dp[2] = [a, aa], [b, bb], [c, cc]

print(max(dp[0][0], dp[1][0], dp[2][0]), end=" ")
print(min(dp[0][1], dp[1][1], dp[2][1]))