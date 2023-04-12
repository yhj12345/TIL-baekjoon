import sys
sys.setrecursionlimit = 10 ** 5

def dfs(cost, depth):
    global flag
    if cost == total // 2:
        flag = True
        return
    if cost > total // 2:
        return
    if depth == N:
        return
    
    if visited[depth][cost]:
        return
    
            
    visited[depth][cost] = True

    for j in range(coin[depth][1]+1):
        if cost + (j * coin[depth][0]) > total // 2:
                break
        
        if depth<N and visited[depth+1][cost +(j * coin[depth][0])]:
          break
        dfs(cost + (j * coin[depth][0]), depth+1)
                

for i in range(3):
    N = int(input())
    coin = [list(map(int, input().split())) for _ in range(N)]
    coin.sort(reverse=True)
    total = 0
    flag = False
    visited = [[False for _ in range(50001)] for _ in range(N+1) ]

    for c, cnt in coin:
        total += c * cnt

    if total % 2 != 0:
        print(0)
    else:
        dfs(0, 0)
        if flag:
            print(1)
        else:
            print(0)
