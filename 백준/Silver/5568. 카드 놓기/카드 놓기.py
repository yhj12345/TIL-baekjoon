from itertools import combinations, permutations

n = int(input())
k = int(input())
number = list(input() for _ in range(n))
result = set()
for combi in combinations(number, k):
    for permu in permutations(combi, k):
        tmp = ''
        for p in permu:
            tmp += p
        result.add(tmp)
print(len(result))