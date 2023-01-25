import copy

def press(array, index):
  if array[index-1] == '0':
    array[index-1] = '1'
  else:
    array[index-1] = '0'
  
  if array[index] == '0':
    array[index] = '1'
  else:
    array[index] = '0'
  
  if index < N-1:
    if array[index+1] == '0':
      array[index+1] = '1'
    else:
      array[index+1] = '0'
  


N = int(input())
now = list(input())
copy_now = copy.deepcopy(now)
make = list(input())

# 0번 스위치를 누르지 않았을 때
result1 = -1
tmp = 0
for i in range(1, N):
  if now[i-1] != make[i-1]:
    tmp += 1
    press(now, i)
flag = True
for i in range(N):
  if now[i] != make[i]:
    flag = False
if flag == True:
  result1 = tmp

# 0번 스위치를 누르고 시작
result2 = -1
tmp = 1
for i in range(2):
  if copy_now[i] == '0':
    copy_now[i] = '1'
  else:
    copy_now[i] = '0'

for i in range(1, N):
  if copy_now[i-1] != make[i-1]:
    tmp += 1
    press(copy_now, i)
flag = True
for i in range(N):
  if copy_now[i] != make[i]:
    flag = False
if flag == True:
  result2 = tmp

if result1 == -1 and result2 == -1:
  print(-1)
elif result1 == -1 and result2 != -1:
  print(result2)
elif result1 != -1 and result2 == -1:
  print(result1)
else:
  print(min(result1, result2))