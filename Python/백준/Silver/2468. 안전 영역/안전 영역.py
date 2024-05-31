from collections import deque
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x,y,h):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if not visited[nx][ny] and graph[nx][ny] > h:
                visited[nx][ny] = True
                queue.append((nx,ny))

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

result = 0
for i in range((max(map(max, graph)))):
    visited = [[False] * N for _ in range(N)]
    cnt = 0

    for j in range(N):
        for k in range(N):
            if graph[j][k] > i and not visited[j][k]:
                bfs(j,k,i)
                cnt += 1

    result = max(result, cnt)

print(result)