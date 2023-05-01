def dfs(depth, array, start):
    if depth == M:
        print(*array)
        return

    for i in range(start, N):
        dfs(depth+1, array+[arr[i]], i)

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
dfs(0, [], 0)