#10423 전기가 부족해

import sys
input = sys.stdin.readline

def find(x):
    if x == root[x]:
        return x
    else:
        root[x] = find(root[x])
        return root[x]

def union(x,y):
    x = find(x)
    y = find(y)

    root[y] = x

n, m, k = map(int, input().split())
power = list(map(int, input().split()))
edges = [list(map(int, input().split())) for _ in range(m)]
edges.sort(key=lambda x:x[2])

root = [i for i in range(n+1)]
for p in power:
    root[p] = 0

result = 0
for x, y, cost in edges:
    if find(x) == find(y):
        continue
        
    union(x,y)
    result += cost

print(result)