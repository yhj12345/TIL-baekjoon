def xor(x, y):
    for i in range(x+1):
        for j in range(y+1):
            arr[i][j] ^= 1

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
answer = 0

for i in range(N-1, -1, -1):
    for j in range(M-1, -1, -1):
        if arr[i][j] == 1:
            answer += 1
            xor(i, j)

print(answer)