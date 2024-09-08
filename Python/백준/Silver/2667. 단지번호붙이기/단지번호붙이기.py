#2667
import sys
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(a,b):
    queue = [(a,b)]
    cnt = 1
    visitied[a][b] = True
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if not visitied[nx][ny] and graph[nx][ny] == 1:
                cnt += 1
                visitied[nx][ny] = True
                queue.append((nx,ny))

    return cnt

N = int(input())
graph = [list(map(int, input().strip())) for _ in range(N)]
visitied = [[False] * N for _ in range(N)]

res = []
for i in range(N):
    for j in range(N):
        if not visitied[i][j] and graph[i][j]:
            res.append(bfs(i,j))

res.sort()
print(len(res))
for num in res:
    print(num)