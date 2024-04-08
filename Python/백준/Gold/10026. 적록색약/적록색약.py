from collections import deque
import sys
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(x,y,color):
    visited[x][y] = True
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= n or nx < 0 or ny >= n or ny < 0:
                continue

            if colors[nx][ny] == color and visited[nx][ny] == False:
                visited[nx][ny] = True
                queue.append((nx,ny))


n = int(input())
colors = [list(input().strip()) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
three_cnt, two_cnt = 0, 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j, colors[i][j])
            three_cnt += 1

for i in range(n):
    for j in range(n):
        visited[i][j] = False
        if colors[i][j] == 'R':
            colors[i][j] = 'G'

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j, colors[i][j])
            two_cnt += 1

print(three_cnt, two_cnt)