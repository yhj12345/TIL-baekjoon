while True:
  password = input()
  if password == 'end':
    break
  
  # 모음이 하나를 반드시 포함
  flag1 = False
  mo = ['a', 'e', 'i', 'o', 'u']
  for m in mo:
    if m in password:
      flag1 = True
      break
  
  # 모음이 3개 혹은 자음이 3개 연속으로 오면 안됨
  flag2 = True
  cnt1, cnt2 = 0, 0
  for p in password:
    if p in mo:
      cnt1 += 1
      cnt2 = 0
    else:
      cnt1 = 0
      cnt2 += 1

    if cnt1 == 3 or cnt2 == 3:
      flag2 = False
      break
  
  # 같은 글자가 연속적으로 두번 오면 안되나, ee와 oo는 허용
  flag3 = True
  for i in range(len(password)-1):
    if password[i] == password[i+1]:
      if password[i] == 'e' or password[i] == 'o':
        continue
      else:
        flag3 = False
  if flag1 and flag2 and flag3:
    print(f'<{password}> is acceptable.')
  else:
    print(f'<{password}> is not acceptable.')