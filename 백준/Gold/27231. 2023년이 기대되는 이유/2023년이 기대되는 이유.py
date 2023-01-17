import sys


def dfs(cal, keep, depth):
  if depth == len(number):
    cal_set.add(cal+keep)
    return
  dfs(cal + (keep * 10) + int(number[depth]), 0, depth + 1)
  dfs(cal, (keep * 10) + int(number[depth]), depth + 1)


def power_number(array, n):
  result = 0
  for i in array:
    result += int(i) ** n
  return result

T = int(input())
for _ in range(T):
  number = list(input())
  only_one_zero = True
  for i in range(len(number)):
    if number[i] != '0' and number[i] != '1':
      only_one_zero = False
      break
  # print(only_one_zero)
  cal_set = set()
  dfs(0, 0, 0)
  limit = max(cal_set)
  n = 1
  flag = False
  answer = 0
  while True:
    power_n_number = power_number(number, n)
    if power_n_number > limit:
      break
    if power_n_number in cal_set:
      answer += 1
    n += 1
    if only_one_zero:
      if answer > 0:
        flag =True
      break
  if flag == True:
    print('Hello, BOJ 2023!')
  else:
    print(answer)