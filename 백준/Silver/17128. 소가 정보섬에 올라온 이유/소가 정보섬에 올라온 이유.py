N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cal = []
for i in range(N):
    cal.append(A[i%N] * A[(i+1)%N] * A[(i+2)%N] * A[(i+3)%N])
result = sum(cal)

for i in range(Q):
    cal[(B[i]-4)%N] *= -1
    cal[(B[i]-3)%N] *= -1
    cal[(B[i]-2)%N] *= -1
    cal[(B[i]-1)%N] *= -1
    result += 2*cal[(B[i]-1)%N] + 2*cal[(B[i]-2)%N] + 2*cal[(B[i]-3)%N] + 2*cal[(B[i]-4)%N]
    print(result)