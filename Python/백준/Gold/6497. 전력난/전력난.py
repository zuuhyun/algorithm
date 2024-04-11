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

while True:
    n,m = map(int, input().split())
    if m == 0 and n == 0:
        break
    root = [i for i in range(n)]
    homes = [list(map(int, input().split())) for _ in range(m)]


    homes = sorted(homes, key=lambda x:x[2])
    result = 0
    for home in homes:
        if find(home[0]) == find(home[1]):
            result += home[2]
            continue
        else:
            union(home[0], home[1])

    print(result)