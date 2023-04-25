def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

N = int(input())
arr = [list(input()) for _ in range(N)]
big = [chr(65+i) for i in range(26)]
small = [chr(97+i) for i in range(26)]
new_arr = [[0 for _ in range(N)] for _ in range(N)]

answer = 0
edges = []
for i in range(N):
    for j in range(N):
        if arr[i][j] in big:
            new_arr[i][j] = ord(arr[i][j]) - 38
        elif arr[i][j] in small:
            new_arr[i][j] = ord(arr[i][j]) - 96

        answer += new_arr[i][j]

        if i != j and new_arr[i][j] != 0:
            edges.append((new_arr[i][j], i, j))

edges.sort()
parent = [i for i in range(N)]
cnt = 0
for cost, a, b in edges:
    if find(a) != find(b):
       answer -= cost
       union(a, b)
       cnt += 1

if cnt == N-1:
    print(answer)
else:
    print(-1) 