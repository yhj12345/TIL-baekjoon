import heapq

def solution(n, k, enemy):
    answer = 0
    heap = []
    
    for e in enemy:
        answer += 1
        
        if len(heap) < k:
            heapq.heappush(heap, e)
        
        else:
            if heap[0] < e:
                a = heapq.heappop(heap)
                heapq.heappush(heap, e)
        
                n -= a
            else:
                n -= e
                
        if n == 0:
            break
        elif n < 0:
            answer -=1
            break
            
    return answer