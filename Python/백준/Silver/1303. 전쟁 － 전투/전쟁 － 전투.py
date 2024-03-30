from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, team):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0
    cnt = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue

            if graph[nx][ny] == team:
                queue.append((nx,ny))
                graph[nx][ny] = 0
                cnt += 1
    return cnt

n, m = map(int, input().split())
graph = []
for _ in range(m):
    graph.append(list(input()))

W, B = 0, 0
for x in range(m):
    for y in range(n):
        if graph[x][y] == 'W':
            W += bfs(x,y,'W')**2
        elif graph[x][y] == 'B':
            B += bfs(x,y,'B')**2

print(W,B)