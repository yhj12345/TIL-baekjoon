N = int(input())
arr = list(map(int, input().split()))

bnp = 0
b_money = N

for i in arr:
    a, b = divmod(b_money, i)
    bnp += a
    b_money = b

timing = 0
t_money = N
new_arr = [0 for _ in range(14)]
for i in range(1, 14):
    new_arr[i] = arr[i] - arr[i-1]
flow = 0
for i in range(14):
    if new_arr[i] == 0:
        flow = 0
    elif new_arr[i] > 0:
        if flow < 0:
            flow = 0
        flow += 1
    else:
        if flow > 0:
            flow = 0
        flow -= 1
    
    if flow <= -3:
        a, b = divmod(t_money, arr[i])
        timing += a
        t_money = b
    elif flow >= 3:
        t_money += arr[i] * timing
        timing = 0

bnp = bnp * arr[-1] + b_money
timing = timing * arr[-1] + t_money
if bnp > timing:
    print('BNP')
elif bnp < timing:
    print('TIMING')
else:
    print("SAMESAME")