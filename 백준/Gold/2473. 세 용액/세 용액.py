import sys

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

result = 10 ** 10
ans = []

for i in range(N-2):
    a = arr[i]
    left, right = i + 1, N-1

    while left < right:
        tmp = a + arr[left] + arr[right]

        if abs(tmp) <= abs(result):
            ans = [a, arr[left], arr[right]]
            result = a + arr[left] + arr[right]
        
        if tmp < 0:
            left += 1
        elif tmp > 0:
            right -= 1
        else:
            print(*ans)
            sys.exit()

print(*ans)