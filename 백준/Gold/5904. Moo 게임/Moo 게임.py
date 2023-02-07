def sol(moo, cnt, N):
  prev = (moo - cnt) // 2
  if N <= prev:
    return sol(prev, cnt-1, N)
  elif N > prev + cnt:
    return sol(prev, cnt-1, N - prev - cnt)
  else: return 'o' if N-prev-1 else 'm'

N = int(input())

moo = 3
depth = 0
while moo < N:
  depth += 1
  moo = moo + depth+3 + moo
print(sol(moo, depth+3, N))