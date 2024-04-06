from collections import deque
import sys
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(i,j):
    queue = deque()
    queue.append((i,j))
    graph[i][j] = 0
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx,ny))
                cnt += 1

    return cnt


n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]
answer = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            answer.append(bfs(i,j))

answer.sort()
print(len(answer))
for ans in answer:
    print(ans)