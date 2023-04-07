N, M = map(int, input().split())
lamp = []
for i in range(N):
    tmp = list(map(int, input().split()))

    if tmp[0] == 0:
        lamp.append(set())
    else:
        lamp.append(set(tmp[1:]))

for i in range(N):
    tmp = set()
    for j in range(N):
        if i != j:
            tmp |= lamp[j]
    if len(tmp) == M:
        print(1)
        break
else:
    print(0)