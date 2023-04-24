def dfs(one, two, three, four, five, pprev, prev):
    if one == 0 and two == 0 and three == 0 and four == 0 and five == 0:
        return 1
    
    if dp[one][two][three][four][five][pprev][prev] != -1:
        return dp[one][two][three][four][five][pprev][prev]
    
    dp[one][two][three][four][five][pprev][prev] = 0

    if one >= 1 and pprev != 1 and prev != 1:
        dp[one][two][three][four][five][pprev][prev] += dfs(one-1, two, three, four, five, prev, 1)
    
    if two >= 1 and pprev != 2 and prev != 2:
        dp[one][two][three][four][five][pprev][prev] += dfs(one, two-1, three, four, five, prev, 2)

    if three >= 1 and pprev != 3 and prev != 3:
        dp[one][two][three][four][five][pprev][prev] += dfs(one, two, three-1, four, five, prev, 3)

    if four >= 1 and pprev != 4 and prev != 4:
        dp[one][two][three][four][five][pprev][prev] += dfs(one, two, three, four-1, five, prev, 4)

    if five >= 1 and pprev != 5 and prev != 5:
        dp[one][two][three][four][five][pprev][prev] += dfs(one, two, three, four, five-1, prev, 5)

    return dp[one][two][three][four][five][pprev][prev]
    

N = int(input())
arr = list(int(input()) for _ in range(N))
while len(arr) < 5:
    arr.append(0)

dp = [[[[[[[-1 for _ in range(6)] for _ in range(6)] for _ in range(11)] for _ in range(11)] for _ in range(11)] for _ in range(11)] for _ in range(11)]
print(dfs(arr[0], arr[1], arr[2], arr[3], arr[4], 0, 0))