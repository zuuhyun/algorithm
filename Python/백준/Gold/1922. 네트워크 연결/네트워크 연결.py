import sys
input = sys.stdin.readline

def find(x):
    if root[x] == x:
        return x
    else:
        root[x] = find(root[x])
        return root[x]

def union(x,y):
    x = find(x)
    y = find(y)

    root[y] = x


N = int(input())
M = int(input())
edges = [list(map(int, input().split())) for _ in range(M)]
edges = sorted(edges, key=lambda x:x[2])

root = {}
for i in range(1, N+1):
    root[i] = i

total_cost = 0
for edge in edges:
    if find(edge[0]) == find(edge[1]):
        continue
    else:
        total_cost += edge[2]
        union(edge[0], edge[1])

print(total_cost)