N = int(input())
number = int(input())

x, y = 0, 0
now = N ** 2
arr = [[0 for _ in range(N)] for _ in range(N)]
arr[x][y] = now

d_dict = dict()
d_dict[0] = N-1
d_dict[1] = 0
d_dict[2] = 1
d_dict[3] = N-1

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

direction = 3
resultX, resultY = 0, 0
while True:
    now -= 1
    if now == 0:
        break
    
    x += dx[direction]
    y += dy[direction]

    arr[x][y] = now

    if now == number:
        resultX = x
        resultY = y

    if direction == 0:
        if y == d_dict[direction]:
            d_dict[direction] -= 1
            direction = 1
    elif direction == 1:
        if x == d_dict[direction]:
            d_dict[direction] += 1
            direction = 2
    elif direction == 2:
        if y == d_dict[direction]:
            d_dict[direction] += 1
            direction = 3
    else:
        if x == d_dict[direction]:
            d_dict[direction] -= 1
            direction = 0
    
for i in range(N):
    print(*arr[i])
print(resultX+1, resultY+1)