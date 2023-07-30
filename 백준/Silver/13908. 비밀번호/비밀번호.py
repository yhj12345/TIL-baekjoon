def dfs(password):
    global ans
    if len(password) == n:
        for num in arr:
            if num not in password:
                break
        else:
            ans += 1
        return
    
    for i in range(10):
        dfs(password+[i])

n, m = map(int, input().split())
if m == 0:
    print(10 ** n)
else:
    arr = list(map(int, input().split()))

    ans = 0
    dfs([])
    print(ans)