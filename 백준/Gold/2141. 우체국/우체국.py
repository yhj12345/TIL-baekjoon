N = int(input())
arr = []
all_people = 0
for _ in range(N):
    X, A = map(int, input().split())
    all_people += A
    arr.append([X, A])

arr.sort(key=lambda x: x[0])
now = 0
half_people = all_people / 2

for i in range(N):
    now += arr[i][1]

    if now >= half_people:
        print(arr[i][0])
        break