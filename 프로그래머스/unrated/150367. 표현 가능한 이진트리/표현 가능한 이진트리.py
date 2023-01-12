from collections import deque

def solution(numbers):
    def dfs(start, end):
      global flag
      if start == end:
        if binary_number_list[start] == '0':
          return False
        else:
          return True
      mid = (start + end) // 2
      a = dfs(start, mid-1)
      b = dfs(mid+1, end)
      if binary_number_list[mid] == '0':
        if a == True or b == True:
          flag = False
        return False
      else:
        return True
    global flag
    answer = []
    for number in numbers:
      binary_number = bin(number)[2:]
      binary_number_list = deque(list(str(binary_number)))
      binary_number_list_length = len(binary_number_list)

      n = 1
      while True:
        if (binary_number_list_length - 1) // ((2 ** n) - 1) == 0: 
          interval = (2 ** n) - 1 - binary_number_list_length 
          break
        else:
          n += 1
      while interval > 0:
        binary_number_list.appendleft('0')
        interval -= 1
      flag = True
      dfs(0, len(binary_number_list)-1)
      if flag == True:
        answer.append(1)
      else:
        answer.append(0)
    return answer

print(solution([63, 111, 95]))