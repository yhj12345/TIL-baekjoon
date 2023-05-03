import heapq

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key = lambda x: (x[0], x[1]))

heap = []
a, b = arr.pop(0)
heapq.heappush(heap, b)
for start, end in arr:
    if heap[0] <= start:
        heapq.heappop(heap)
    heapq.heappush(heap, end)
print(len(heap))