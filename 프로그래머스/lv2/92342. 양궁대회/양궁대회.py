from itertools import product

def solution(n, info):
    answer = [0 for _ in range(11)]
    max_score = 0
    for pro in product((True, False), repeat=11):
        lion = 0
        apeach = 0
        cnt = 0
        
        for i in range(11):
            if pro[i]:
                lion += 10 - i
                cnt += info[i] + 1
            else:
                if info[i] > 0:
                    apeach += 10 - i
                        
        if lion <= apeach:
            continue
        
        if cnt > n:
            continue
        
        if max_score > lion-apeach:
            continue
        
        tmp = [0 for _ in range(11)]
        for i in range(11):
            if pro[i]:
                tmp[i] = info[i] + 1
        
        cnt = sum(tmp)
        
        tmp[10] += n-cnt
        
        if max_score < lion-apeach:
            answer = tmp
            max_score = lion-apeach
        else:
            for i in range(10, -1, -1):
                if answer[i] < tmp[i]:
                    answer = tmp
                    break
                elif answer[i] > tmp[i]:
                    break
                    
    if sum(answer) == 0:
        answer = [-1]
    return answer