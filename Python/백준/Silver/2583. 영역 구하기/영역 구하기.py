import sys
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
    queue = [(x,y)]
    visited[y][x] = True
    area_size = 0

    while queue:
        x, y = queue.pop(0)
        area_size += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append((nx,ny))

    return area_size

M, N, K = map(int, input().split())
visited = [[False] * N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            visited[y][x] = True

areas = []
for x in range(N):
    for y in range(M):
        if not visited[y][x]:
            area_size = bfs(x,y)
            areas.append(area_size)

areas.sort()
print(len(areas))
print(*areas)