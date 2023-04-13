from collections import defaultdict

while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    
    ranking = defaultdict(int)
    for i in range(N):
        week = list(map(int, input().split()))
        for w in week:
            ranking[w] += 1
    
    sorted_ranking = sorted(ranking.items(), key=lambda x: x[1], reverse=True)
    result = [sorted_ranking[1][0]]
    point = sorted_ranking[1][1]
    for i in range(2, len(sorted_ranking)):
        if point == sorted_ranking[i][1]:
            result.append(sorted_ranking[i][0])
        else:
            break
    result.sort()
    print(*result)
