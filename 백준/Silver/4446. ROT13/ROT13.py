mo = ['a', 'i', 'y', 'e', 'o', 'u']
da_mo = ['A', 'I', 'Y', 'E', 'O', 'U']
ja = ['b', 'k', 'x', 'z', 'n', 'h', 'd', 'c', 'w', 'g', 'p', 'v', 'j', 'q', 't', 's', 'r', 'l', 'm', 'f']
da_ja = ['B', 'K', 'X', 'Z', 'N', 'H', 'D', 'C', 'W', 'G', 'P', 'V', 'J', 'Q', 'T', 'S', 'R', 'L', 'M', 'F']
while True:
  try:
    sentence = list(input())
    for i in range(len(sentence)):
      if sentence[i] in mo:
        a = mo.index(sentence[i])
        new_a = (a + 3) % 6
        sentence[i] = mo[new_a]
      elif sentence[i] in da_mo:
        a = da_mo.index(sentence[i])
        new_a = (a + 3) % 6
        sentence[i] = da_mo[new_a]
      elif sentence[i] in ja:
        a = ja.index(sentence[i]) 
        new_a = (a + 10) % 20
        sentence[i] = ja[new_a]
      elif sentence[i] in da_ja:
        a = da_ja.index(sentence[i]) 
        new_a = (a + 10) % 20
        sentence[i] = da_ja[new_a]
    print(''.join(sentence))
  except:
    break