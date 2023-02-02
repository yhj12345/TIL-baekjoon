import sys
sys.setrecursionlimit(10**5)

def pre_order(in_start, in_end, post_start, post_end):
  if in_start > in_end or post_start > post_end:
    return
  root = post_order[post_end]
  print(root, end=" ")

  idx = position[root]
  left = idx - in_start
  right = in_end - idx

  pre_order(in_start, in_start + left - 1, post_start, post_start + left - 1)
  pre_order(in_end - right + 1, in_end, post_end - right, post_end -1 )
  return

n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

position = [0] * (n+1)
for i in range(n):
  position[in_order[i]] = i

pre_order(0, n-1, 0, n-1)
