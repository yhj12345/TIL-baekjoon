N, K = map(int, input().split())
arr = list(map(int, input().split()))

cal_sum = 0
dict_sum = {0: 1}
result = 0

for i in range(N):
  cal_sum += arr[i]
  if cal_sum - K in dict_sum:
    result += dict_sum[cal_sum - K]
  if cal_sum in dict_sum:
    dict_sum[cal_sum] += 1
  else:
    dict_sum[cal_sum] = 1
print(result)