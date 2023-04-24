import heapq

def dijkstra(start):
    distance[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        dist, now = heapq.heappop(heap)

        if distance[now] < dist:
            continue
        
        for next, cost in graph[now]:
            if distance[next] > dist + cost:
                distance[next] = dist + cost
                heapq.heappush(heap, (dist+cost, next))

N, M = map(int, input().split())
arr = list(map(int, input().split()))
see = set()
for i in range(1, N-1):
    if arr[i] == 1:
        see.add(i)

graph = [[] for _ in range(N)]
INF = int(1e20)
distance = [INF for _ in range(N)]

for _ in range(M):
    a, b, c = map(int, input().split())
    if a not in see and b not in see:
        graph[a].append((b, c))
        graph[b].append((a, c))

dijkstra(0)
if distance[N-1] == INF:
    print(-1)
else:
    print(distance[N-1])