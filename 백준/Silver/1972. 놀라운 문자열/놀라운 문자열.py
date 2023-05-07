while True:
    S = input()
    if S == '*':
        break
    n = len(S)
    
    flag = True
    for i in range(n-2):
        D_set = set()

        # 0 0 0 0 0
        for j in range(n-i-1):
            tmp = S[j] + S[j+i+1]

            if tmp in D_set:
                flag = False
                break
            else:
                D_set.add(tmp)
        
        if flag == False:
            break
    if flag:
        print(f'{S} is surprising.')
    else:
        print(f'{S} is NOT surprising.')
