import heapq

N = int(input())
min_heap = []
max_heap = []

for i in range(N):
    P, L = map(int, input().split())
    heapq.heappush(min_heap, (L, P))
    heapq.heappush(max_heap, (-L, -P))

M = int(input())
solved = set()

for i in range(M):
    command = list(input().split())
    if command[0] == 'solved':
        solved.add(int(command[1]))
    
    elif command[0] == 'add':
        while -max_heap[0][1] in solved:
                L, P = heapq.heappop(max_heap)

        while min_heap[0][1] in solved:
                L, P = heapq.heappop(min_heap)
                
        if int(command[1]) in solved:
            solved.remove(int(command[1]))
        
        heapq.heappush(min_heap, (int(command[2]), int(command[1])))
        heapq.heappush(max_heap, (-int(command[2]), -int(command[1])))

    else:
        if command[1] == '1':
            while -max_heap[0][1] in solved:
                L, P = heapq.heappop(max_heap)
            print(-max_heap[0][1])

        else:
            while min_heap[0][1] in solved:
                L, P = heapq.heappop(min_heap)
            print(min_heap[0][1])
