'''
bfs() 사용 
출력: 그림의 개수, 가장 넒은 그림의 넓이
'''
from collections import deque
import sys
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
    queue = deque()
    visited[x][y] = True
    queue.append((x,y))
    art = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 1 and visited[nx][ny] == False:
                art += 1
                visited[nx][ny] = True
                queue.append((nx,ny))

    return art


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

cnt, ans = 0, 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == False:
            cnt += 1
            ans = max(bfs(i,j), ans)

print(cnt)
print(ans)
