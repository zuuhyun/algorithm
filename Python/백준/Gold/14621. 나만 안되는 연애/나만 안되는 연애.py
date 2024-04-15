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

N, M = map(int, input().split())
univ = [0] + list(input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
edges = sorted(edges, key=lambda x:x[2])
root = [i for i in range(N+1)]

path_sum, path_num = 0, 0
for x, y, cost in edges:
    if find(x) == find(y) or univ[x] == univ[y]:
        continue

    union(x, y)
    path_sum += cost
    path_num += 1


if path_num == N-1:
    print(path_sum)
else:
    print(-1)