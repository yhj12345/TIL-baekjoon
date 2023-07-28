def check_eggs(index, eggs):
    count = 1

    for idx, egg in enumerate(eggs):
        if idx == index:
            continue
        
        if egg <= 0:
            count += 1
    
    if count == N:
        return True
    else:
        return False
    
def create_new_eggs(idx1, idx2, eggs):
    tmp = eggs[:]
    tmp[idx1] -= W[idx2]
    tmp[idx2] -= W[idx1]
    return tmp

def count_break_eggs(eggs):
    cnt = 0
    for egg in eggs:
        if egg <= 0:
            cnt += 1
    return cnt


def dfs(depth, eggs):
    global ans
    if depth == N:
        break_egg = count_break_eggs(eggs)
        ans = max(ans, break_egg)
        return
    
    if eggs[depth] <= 0 or check_eggs(depth, eggs):
        dfs(depth+1, eggs)
    else:
        for i in range(N):
            if depth == i:
                continue
            
            if eggs[i] <= 0:
                continue
            
            new_eggs = create_new_eggs(depth, i, eggs)
            dfs(depth+1, new_eggs)

N = int(input())
S = [0 for _ in range(N)]
W = [0 for _ in range(N)]

for i in range(N):
    S[i], W[i] = map(int, input().split())

ans = 0
dfs(0, S)
print(ans)