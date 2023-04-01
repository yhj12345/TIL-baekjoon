def solution(plans):
    answer = []
    
    time_table = []
    for plan in plans:
        hour, minute = map(int, plan[1].split(':'))
        time = hour * 60 + minute
        
        time_table.append([time, plan[0], int(plan[2])])
    time_table.sort(reverse=True)
    
    working = [time_table.pop()]
    
    while time_table:
        next_time, next_name, next_playtime = time_table.pop()
        prev_time, prev_name, prev_playtime = working[-1]
        
        tmp = next_time - prev_time
            
        while tmp > 0 and working:
            if tmp >= working[-1][2]:
                a, b, c = working.pop()
                tmp -= c
                answer.append(b)
            else:
                working[-1][2] -= tmp
                break
        working.append([next_time, next_name, next_playtime])
        
    while working:
        a, b, c = working.pop()
        answer.append(b)
        
    
    return answer