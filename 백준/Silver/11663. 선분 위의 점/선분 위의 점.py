import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

for _ in range(M):
    s, e = map(int, input().split())
    left = bisect_left(arr, s)
    right = bisect_right(arr, e)
    print(right-left)