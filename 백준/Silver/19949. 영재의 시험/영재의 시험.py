def dfs(depth):
    global cnt
    if depth == 10:
        s = 0
        for j in range(10):
            if li[j] == ans[j]:
                s += 1
        if s >= 5:
            cnt += 1
        return ;
    for i in range(1, 6):
        if depth > 1 and li[depth-2] == li[depth-1] == i:
            continue
        li.append(i)
        dfs(depth+1)
        li.pop()
        
ans = list(map(int, input().split()))
li, cnt = [], 0
dfs(0)
print(cnt)