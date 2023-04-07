N, C, W = map(int, input().split())
arr = [int(input()) for _ in range(N)]

max_length = max(arr)
answer = 0
for i in range(1, max_length+1):
    tmp = 0
    for j in range(N):
        a, b = divmod(arr[j], i)
        in_money = a * W * i
        if b == 0:
            out_money = (a-1) * C
        else:
            out_money = a * C

        if in_money > out_money:
            tmp += in_money-out_money

    answer = max(answer, tmp)
print(answer)