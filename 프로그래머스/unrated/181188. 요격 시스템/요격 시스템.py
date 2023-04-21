def solution(targets):
    answer = 1
    
    def inter(a, b):
        if b[1] <= a[0]:
            return -1
        else:
            next = [max(a[0], b[0]), min(a[1], b[1])]
            return next
    
    targets.sort(key = lambda x : (-x[1], -x[0]))
    now = targets[0]
    
    for i in range(1, len(targets)):
        tmp = inter(now, targets[i])
        if tmp == -1:
            now = targets[i]
            answer += 1
        else:
            now = tmp
    return answer