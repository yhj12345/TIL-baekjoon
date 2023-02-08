R, C, W = map(int, input().split())
pascal = [[] for _ in range(30)]
pascal[0].append(1)
for i in range(1, 30):
  pascal[i].append(1)
  for j in range(i-1):
    pascal[i].append(pascal[i-1][j] + pascal[i-1][j+1])
  pascal[i].append(1)

ans = 0
tmp = 1
for i in range(R-1, R+W-1):
  for j in range(C-1, C+tmp-1):
    ans += pascal[i][j]
  tmp += 1
print(ans)