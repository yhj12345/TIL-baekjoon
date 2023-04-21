# def solution(r1, r2):
#     answer = 4
#     for i in range(r1, r2):
#         if i >=4 and r2-1 == i:
#             answer += i* 8 - 4
#         else:
#             answer += i * 8
        
#     return answer

import math

def solution(r1, r2):
    answer = 0
    
    for i in range(-r2, r2+1):
        
        answer += 2 * math.floor((r2**2-i**2) ** 0.5)  + 1 ;
        # print( answer)
        
        if abs(i)<r1:  answer -=  2* (math.ceil((r1**2-i**2) ** 0.5)-1) + 1
        
    return answer