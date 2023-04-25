N, ATK = map(int, input().split())

room_info = [list(map(int, input().split())) for _ in range(N)]
damage = []

for t, a, h in room_info:
    if t == 1:
        x, y = divmod(h, ATK)
        if y == 0:
            damage.append((x-1) * a)
        else:
            damage.append(x * a)
    else:
        damage.append(-h)
        ATK += a
left = 0
right = 10 ** 20

answer = 10 ** 20
while left <= right:
    mid = (left + right) // 2
    tmp = mid

    for i in range(len(damage)):
        if damage[i] > 0:
            tmp -= damage[i]
            if tmp <= 0:
                break
        
        else:
            if mid >= tmp - damage[i]:
                tmp -= damage[i]
            else:
                tmp = mid
    
    if tmp >= 1:
        answer = min(answer, mid)
        right = mid-1
    else:
        left = mid+1

print(answer)
    