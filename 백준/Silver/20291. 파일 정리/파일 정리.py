from collections import defaultdict

N = int(input())
files = defaultdict(int)
for i in range(N):
    name, extension = input().split('.')
    files[extension] += 1

sorted_files = sorted(files)
for i in range(len(sorted_files)):
    print(sorted_files[i], files[sorted_files[i]])