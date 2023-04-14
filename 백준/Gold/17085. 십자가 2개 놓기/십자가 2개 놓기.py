dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def find_cross(x, y):
    size = 0
    cross = []
    while True:
        tmp = 0
        cross.append([size, x, y])
        size += 1
        for k in range(4):
            nx = x + (dx[k] * size)
            ny = y + (dy[k] * size)

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if arr[nx][ny] == '#':
                tmp += 1
        if tmp != 4:
            break
    return cross

def match(a, b):
    a_list = []
    a_cnt, b_cnt = 0, 0
    while a[0] >= a_cnt:
        for k in range(4):
            nx = a[1] + dx[k] * a_cnt
            ny = a[2] + dy[k] * a_cnt

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            
            a_list.append((nx, ny))
        a_cnt += 1

    while b[0] >= b_cnt:
        for k in range(4):
            nx = b[1] + dx[k] * b_cnt
            ny = b[2] + dy[k] * b_cnt

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if (nx, ny) in a_list:
                return False
        b_cnt += 1
    return True

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

crosses = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == '#':
            tmp = find_cross(i, j)
            crosses += tmp

ans = 0
for i in range(len(crosses)):
    for j in range(i+1, len(crosses)):
        width = (1 + (4 * crosses[i][0])) * (1 + (4 * crosses[j][0]))

        if width > ans:
            is_possible = match(crosses[i], crosses[j])

            if is_possible:
                ans = width
print(ans)