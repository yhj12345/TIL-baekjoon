import sys
from itertools import combinations

N, K = map(int, input().split())
word_list = list(set(list(input())) for _ in range(N))
alpha = ['b', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 'u', 'v', 'w', 'x', 'y', 'z']
essentail = set(['a', 't', 'i', 'n', 'c'])
result = 0
if K >= 5:
  for combi in combinations(alpha, K-5):
    new_set = essentail | set(combi)
    tmp = 0
    for i in range(N):
      if word_list[i] <= new_set:
        tmp += 1
    result = max(tmp, result)

  print(result)
else:
  print(0)