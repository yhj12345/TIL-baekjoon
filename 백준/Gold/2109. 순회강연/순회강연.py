import heapq

n = int(input())
heap = []
for _ in range(n):
    p, d = map(int, input().split())
    heapq.heappush(heap, (d, -p))

now = 1
money = []
while heap:
    day, pay = heapq.heappop(heap)

    if len(money) < day:
        heapq.heappush(money, -pay)
    
    else:
        if money[0] < -pay:
            heapq.heappop(money)
            heapq.heappush(money, -pay)
print(sum(money))