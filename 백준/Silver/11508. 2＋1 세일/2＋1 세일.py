import heapq

N = int(input())

answer = 0
heap = []
for i in range(N):
    c = int(input())
    heapq.heappush(heap, -c)

while len(heap) >= 3:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    c = heapq.heappop(heap)
    answer -= a
    answer -= b

while heap:
    answer -= heapq.heappop(heap)
print(answer)