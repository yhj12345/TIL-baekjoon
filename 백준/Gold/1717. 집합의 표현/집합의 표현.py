import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [0 for _ in range(n+1)]
# 자기 자신을 부모로 설정
for i in range(n+1):
  parent[i] = i

# 루트 노드 찾는 함수
def find(x):
  # 자기 자신이 루트 노드이면 x 반환
  if x == parent[x]:
    return x
  p = find(parent[x])
  parent[x] = p
  return parent[x]

def union(x, y):
  parent_x = find(x)
  parent_y = find(y)

  if parent_x == parent_y:
    return
  if parent_x < parent_y:
    parent[parent_y] = parent_x
  else:
    parent[parent_x] = parent_y

for _ in range(m):
  o, a, b = map(int, input().split())
  if o == 0:
    union(a, b)
  else:
    if find(a) == find(b):
      print('YES')
    else:
      print("NO")