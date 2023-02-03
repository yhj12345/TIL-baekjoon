from collections import defaultdict

N = int(input())
time_dict = defaultdict(int)

for i in range(N):
  Tem, Txm = map(int, input().split())
  time_dict[Tem] += 1
  time_dict[Txm] -= 1

sorted_time_dict = sorted(time_dict.keys())

result = 0
tmp = 0
Tem, Txm = 0, 0
flag = False
for m in sorted_time_dict:
  tmp += time_dict[m]
  if tmp > result:
    result = tmp
    Tem = m
    flag = True
  elif tmp < result and tmp - time_dict[m] == result and flag:
    Txm = m
    flag = False
print(result)
print(Tem, Txm)
