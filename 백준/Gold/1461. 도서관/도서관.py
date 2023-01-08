import sys

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

result = []

minus_tmp = []
minus_index = 0
for i in range(N):
  if arr[i] > 0:
    break
  minus_tmp.append(arr[i])
  if len(minus_tmp) == M:
    result.append(-arr[minus_index])
    minus_tmp = []
    minus_index += M
if len(minus_tmp) > 0:
  result.append(-minus_tmp[0])

plus_tmp = []
plus_index = N-1
for i in range(N-1, -1, -1):
  if arr[i] < 0:
    break
  plus_tmp.append(arr[i])
  if len(plus_tmp) == M:
    result.append(arr[plus_index])
    plus_tmp = []
    plus_index -= M
if len(plus_tmp) > 0:
  result.append(plus_tmp[0])
result.sort()

answer = result[-1]
for i in range(len(result)-1):
  answer += result[i] * 2
print(answer)