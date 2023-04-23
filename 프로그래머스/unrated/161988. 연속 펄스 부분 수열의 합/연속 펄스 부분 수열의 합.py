import heapq

def solution(sequence):
    answer = 0
    N = len(sequence)
    arr1 = []
    arr2 = []
    purse = 1
    for i in range(N):
        arr1.append(sequence[i] * purse)
        arr2.append(sequence[i] * purse * -1)
        purse *= -1
    
    sum_arr1 = [0 for _ in range(N)]
    sum_arr2 = [0 for _ in range(N)]
    sum_arr1[0] = arr1[0]
    sum_arr2[0] = arr2[0]
    for i in range(1, N):
        sum_arr1[i] = sum_arr1[i-1] + arr1[i]
        sum_arr2[i] = sum_arr2[i-1] + arr2[i]
    
    result1 = sum_arr1[0]
    result2 = sum_arr2[0]
    q1 = [sum_arr1[0]]
    q2 = [sum_arr2[0]]
    
    for i in range(1, N):
        if q1[0] < 0:
            tmp = sum_arr1[i] - q1[0]
        else:
            tmp = sum_arr1[i]
        result1 = max(result1, tmp)
        heapq.heappush(q1, sum_arr1[i])
        
        if q2[0] < 0:
            tmp = sum_arr2[i] - q2[0]
        else:
            tmp = sum_arr2[i]
        result2 = max(result2, tmp)
        heapq.heappush(q2, sum_arr2[i])
    answer = max(result1, result2)
    
    return answer