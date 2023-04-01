import heapq

def solution(n, roads, sources, destination):
    answer = []
    INF = 10 ** 6
    
    def dijkstra(start):
        distance = [INF for _ in range(n+1)]
        distance[start] = 0
        q = []
        heapq.heappush(q, (0, start))
        
        while q:
            dist, now = heapq.heappop(q)
            
            if distance[now] < dist:
                continue
            
            for node in graph[now]:
                if distance[node] > dist + 1:
                    distance[node] = dist + 1
                    heapq.heappush(q, (dist + 1, node))
        
        return distance
    
    graph = [[] for _ in range(n+1)]
    
    for s, e in roads:
        graph[s].append(e)
        graph[e].append(s)
        
    result = dijkstra(destination)
    for source in sources:
        if result[source] != INF:
            answer.append(result[source])
        else:
            answer.append(-1)
    
    return answer