import sys
input = sys.stdin.readline

def bfs(V):
    visited[V] = True
    queue = [V]
    answer = 0
    while queue:
        V = queue.pop(0)
        for i in range(1, com+1):
            if graph[V][i] == 1 and visited[i] == False:
                visited[i] = True
                queue.append(i)
                answer += 1

    return answer


com = int(input())
conn = int(input())
graph = [[0] * (com+1) for _ in range(com+1)]
visited = [False] * (com + 1)

for _ in range(conn):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

print(bfs(1))