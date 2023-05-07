from itertools import combinations

def sol(number, cut):
    tmp = str(number)
    a = tmp[:cut[0]]
    b = tmp[cut[0]:cut[1]]
    c = tmp[cut[1]:]

    return int(a) + int(b) + int(c)

def checkodd(number):
    cnt = 0

    while True:
        a, b = divmod(number, 10)
        if a == 0 and b == 0:
            break
        
        if b % 2 == 1:
            cnt += 1
        number = a
    return cnt

def dfs(number, cnt):
    global max_ans, min_ans
    odd_cnt = checkodd(number)

    if number < 10:
        max_ans = max(max_ans, cnt + odd_cnt)
        min_ans = min(min_ans, cnt + odd_cnt)
        return
    
    elif number < 100:
        a = number // 10
        b = number % 10
        dfs(a+b, cnt + odd_cnt)
    
    else:
        for combi in combinations(range(1, len(str(number))), 2):
            tmp = sol(number, combi)
            dfs(tmp, cnt + odd_cnt)

N = int(input())
min_ans = 100000
max_ans = 0
dfs(N, 0)
print(min_ans, max_ans)