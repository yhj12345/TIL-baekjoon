N = int(input())
colors = input()
color = colors[0]
cnt = 1
for i in range(1, N):
    if color != colors[i]:
        color = colors[i]
        cnt += 1

print((cnt // 2) + 1)