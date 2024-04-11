import math
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

n, m = map(int, input().split())
stars = [0] + [list(map(int, input().split())) for _ in range(n)]
root = [i for i in range(n+1)]
conns = [list(map(int, input().split())) for _ in range(m)]

for conn in conns:
    union(conn[0],conn[1])

edges = []
for i in range(1, n):
    for j in range(i+1,n+1):
        cost = math.sqrt((stars[i][0] - stars[j][0])**2 + (stars[i][1] - stars[j][1])**2)
        edges.append([i,j,cost])

edges = sorted(edges, key=lambda x:x[2])
result = 0
for edge in edges:
    if find(edge[0]) != find(edge[1]):
        result += edge[2]
        union(edge[0],edge[1])

print("{:.2f}".format(result))
