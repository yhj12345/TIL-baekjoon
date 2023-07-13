from bisect import bisect_right

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = [0 for _ in range(N)]

for i, a in enumerate(A):
    tmp = bisect_right(B, a)
    result[i] = max(0, tmp - i - 1)

print(*result)