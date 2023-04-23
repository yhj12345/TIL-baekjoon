def solution(sequence, k):
    answer = []
    sum_dict = dict()
    sum_arr = [0 for _ in range(len(sequence))]
    sum_arr[0] = sequence[0]
    for i in range(1, len(sequence)):
        sum_arr[i] = sum_arr[i-1] + sequence[i]
        
    result = []
    for i in range(len(sum_arr)):
        tmp = sum_arr[i] - k
        if tmp == 0:
            result.append((0, i))
        else:
            if tmp in sum_dict:
                result.append((sum_dict[tmp]+1, i))
        
        sum_dict[sum_arr[i]] = i
    
    left, right = result[0]
    for a, b in result:
        if right - left > b - a:
            left = a
            right = b
    answer.append(left)
    answer.append(right)
    
    
    return answer