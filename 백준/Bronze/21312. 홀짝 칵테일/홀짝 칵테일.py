from itertools import combinations

def sol(taste):
    global result
    a = result % 2
    b = taste % 2

    if (a and b) or (not a and not b):
        result = max(result, taste)
    elif not a and b:
        result = taste

arr = list(map(int, input().split()))
result = arr[0]

for i in range(1, 4):
    for combi in combinations(arr, i):
        taste = 1

        for c in combi:
            taste *= c
        sol(taste)
print(result)