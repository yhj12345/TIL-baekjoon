N, K = map(int, input().split())
S = list(map(int, input().split()))
D = list(map(int, input().split()))

for _ in range(K):
    P_dict = dict()
    for i in range(len(D)):
        P_dict[D[i]] = S[i]
    tmp = []
    for i in range(1, len(D)+1):
        tmp.append(P_dict[i])
    S = tmp
print(*S)