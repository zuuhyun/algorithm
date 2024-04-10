'''
Kruskal 이용
Edge cost 오름차순으로 정렬
'''

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

V, E = map(int, input().split())
edge = [list(map(int, input().split())) for _ in range(E)]
edge = sorted(edge, key=lambda x: x[2])


#Union-Find 구현
root = {}
for i in range(1, V+1):
    root[i] = i

total_cost = 0
for eg in edge:
    #사이클이 만들어지는 edge라면 pass
    if find(eg[0]) == find(eg[1]):
        continue
    else:
        total_cost += eg[2]
        union(eg[0], eg[1])

print(total_cost)