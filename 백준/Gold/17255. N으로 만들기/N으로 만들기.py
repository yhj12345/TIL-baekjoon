def isPossible(number):
    flag = True
    count_arr = [0 for _ in range(10)]
    for n in number:
        count_arr[int(n)] += 1

    for i in range(10):
        if count_arr[i] > arr[i]:
            flag = False
            break
    
    return flag

def dfs(depth, number, array):
    global ans
    if depth == M:
        if number == N:
            ans += 1
        return
    
    if depth == 0:
        for i in range(10):
            dfs(depth+1, str(i), (str(i)))
    
    else:
        for i in range(10):
            tmp = number + str(i)
            is_possible = isPossible(tmp)
            if array+(tmp) not in visited and is_possible:
                visited.add(array+(tmp))
                dfs(depth+1, tmp, array+(tmp))
            
            tmp = str(i) + number
            is_possible = isPossible(tmp)
            if array+(tmp) not in visited and is_possible:
                visited.add(array+(tmp))
                dfs(depth+1, tmp, array+(tmp))
    

N = input()
M = len(N)
arr = [0 for _ in range(10)]

for n in N:
    arr[int(n)] += 1

ans = 0
visited = set()
dfs(0, '', ())
print(ans)