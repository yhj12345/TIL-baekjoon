from itertools import combinations

N, M = map(int, input().split())
possible = []

for i in range(N):
    guitar, song = input().split()

    tmp = []
    for i in range(len(song)):
        if song[i] == 'Y':
           tmp.append(i) 
    
    possible.append(tmp)

ans = 0
cnt = 0
for i in range(1, N+1):
    for combi in combinations(possible, i):
        temp = set()
        for c in combi:
            for k in c:
                temp.add(k)
        
        if cnt < len(temp):
            cnt = len(temp)
            ans = i
    if cnt == M:
        break
if ans == 0:
    print(-1)
else: 
  print(ans)