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

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
root = list(i for i in range(n))

edges = []
for i in range(n):
    for j in range(i+1, n):
        edges.append((graph[i][j], i,j))

edges.sort()
cost = 0
for edge, x, y in edges:
    if find(x) == find(y):
        continue
    union(x,y)
    cost+=edge

print(cost)
