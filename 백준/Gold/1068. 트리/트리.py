import sys


def remove(start):
    while len(tree[start]) > 0:
        node = tree[start].pop()
        remove(node)

def count_leef_node(start):
    global result
    if len(tree[start]) == 0:
        result += 1
    
    for node in tree[start]:
        count_leef_node(node)

N = int(input())
tree = [[] for _ in range(N)]
arr = list(map(int, input().split()))
remove_node = int(input())
root = 0
result = 0
for i in range(N):
    if arr[i] == -1:
        root = i
    else:
        tree[arr[i]].append(i)

remove(remove_node)
for i in range(N):
    if remove_node in tree[i]:
        tree[i].remove(remove_node)
count_leef_node(root)
if root == remove_node:
    print(0)
else:
    print(result)