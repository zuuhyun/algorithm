N,M,V = map(int, input().split())

#행렬 만들기
graph = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    v1,v2 = map(int, input().split())
    graph[v1][v2] = graph[v2][v1] = 1

#방문 리스트 행렬
dfs_visited = [0] * (N+1)
bfs_visited = dfs_visited.copy()

#dfs 함수 만들기
def dfs(V):
    dfs_visited[V] = 1
    print(V, end=' ')
    for i in range(1, N+1):
        if graph[V][i] == 1 and dfs_visited[i] == 0:
            dfs(i)

#bfs 함수 만들기
def bfs(V):
    bfs_visited[V] = 1
    queue = [V]
    while queue:
        V = queue.pop(0)
        print(V, end=' ')
        for i in range(1, N+1):
            if graph[V][i] == 1 and bfs_visited[i] == 0:
                queue.append(i)
                bfs_visited[i] = 1

dfs(V)
print()
bfs(V)