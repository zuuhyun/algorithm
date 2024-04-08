import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
queue = deque()


def bfs():
    while queue:
        z, x, y = queue.popleft()
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M or nz < 0 or nz >= H:
                continue
            if graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = graph[z][x][y]+1
                queue.append((nz, nx, ny))


# 탐색은 입력의 반대순으로
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1:
                queue.append((i, j, k))
bfs()

all_ripe = True
day = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 0:
                all_ripe = False
                break
            day = max(day, graph[i][j][k])

if all_ripe:
    print(day-1)
else:
    print(-1)