S = input()
alpha = [0 for _ in range(26)]
for s in S:
    alpha[ord(s)-ord('a')] += 1
print(*alpha)