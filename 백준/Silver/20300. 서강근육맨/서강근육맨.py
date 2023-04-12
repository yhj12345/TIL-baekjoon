N = int(input())
t = list(map(int, input().split()))

t.sort()
result = []
if N % 2 != 0:
    result.append(t.pop())

for i in range(len(t)//2):
    tmp = t[i] + t[len(t)-i-1]
    result.append(tmp)

print(max(result))