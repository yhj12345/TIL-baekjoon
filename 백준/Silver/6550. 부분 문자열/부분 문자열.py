while True:
  try:
    s, t = map(str, input().split())
    s_idx = 0
    cnt = 0
    flag = False
    for i in range(len(t)):
      if s[s_idx] == t[i]:
        cnt += 1
        s_idx += 1
      if s_idx == len(s):
        flag = True
        break
    if flag:
      print('Yes')
    else:
      print('No')
    
  except:
    break