import heapq

def dijkstra(start):
    heap = []
    distance[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        dist, now = heapq.heappop(heap)
        if dist > distance[now]:
            continue
        
        for next, cost in graph[now]:
            if distance[next] > cost + dist:
                distance[next] = cost + dist        
                heapq.heappush(heap, (cost+dist, next))

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
INF = 10 ** 9
distance = [INF for _ in range(N+1)]


for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
dijkstra(1)
print(distance[N])