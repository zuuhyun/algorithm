coms = int(input())
conn = int(input())

graph = [[0]*(coms+1) for _ in range(coms+1)]

for i in range(conn):
    a,b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

visitied = [0] * (coms+1)

def dfs(V):
    visitied[V] = 1
    for i in range(1, coms+1):
        if visitied[i] == 0 and graph[V][i] == 1:
            dfs(i)

dfs(1)
print(sum(visitied) - 1)