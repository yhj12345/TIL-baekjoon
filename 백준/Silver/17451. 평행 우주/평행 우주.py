n = int(input())
v = list(map(int, input().split()))

result = [v[-1]]

for i in range(n-1, 0, -1):
    if result[n-1-i] > v[i-1]:
        a, b = divmod(result[n-1-i], v[i-1])
        tmp = v[i-1] * a
        if b != 0:
            tmp += v[i-1]
        result.append(tmp)
    else:
        result.append(v[i-1])

print(result[-1])