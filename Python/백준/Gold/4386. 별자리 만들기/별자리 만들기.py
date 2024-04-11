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

n = int(input())
stars = [0] + [list(map(float, input().split())) for _ in range(n)]
root = [i for i in range(n+1)]

edge = []
for i in range(1, n):
    for j in range(i+1, n+1):
        cost = math.sqrt((stars[i][0] - stars[j][0])**2 + (stars[i][1] - stars[j][1])**2)
        edge.append([i,j,cost])

edge = sorted(edge, key=lambda x:x[2])

result = 0
for eg in edge:
    if find(eg[0]) == find(eg[1]):
        continue
    else:
        result += eg[2]
        union(eg[0],eg[1])


print("{:.2f}".format(result))
