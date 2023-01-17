import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(M):
  ask_number = int(input())
  if ask_number < N:
    print(arr[ask_number])
  else:
    ask_number -= V - 1
    ask_number = ask_number % (N-V+1)
    print(arr[ask_number+ V-1])