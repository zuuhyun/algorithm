import sys
input = sys.stdin.readline

def dfs(V):
    dfs_visited[V] = 1
    print(V, end= ' ')
    for i in range(1, N+1):
        if graph[V][i] == 1 and dfs_visited[i] == 0:
            dfs(i)

def bfs(V):
    bfs_visited[V] = 1
    queue = [V]
    while queue:
        V = queue.pop(0)
        print(V, end =' ')
        for i in range(1, N+1):
            if graph[V][i] == 1 and bfs_visited[i] == 0:
                bfs_visited[i] = 1
                queue.append(i)


N,M,V = map(int, input().split())
graph = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

dfs_visited = [0] * (N+1)
bfs_visited = dfs_visited.copy()

dfs(V)
print()
bfs(V)