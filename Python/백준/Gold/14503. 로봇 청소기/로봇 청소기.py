dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
x, y, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

visited[x][y] = True
cnt = 1

while True:
    flag = False
    for _ in range(4):
        d = (d+3) % 4
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0 and not visited[nx][ny]:
            visited[nx][ny] = True
            cnt += 1
            x, y = nx, ny
            flag = True
            break

    if not flag:
        nx = x - dx[d]
        ny = y - dy[d]
        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
            x, y = nx, ny
        else:
            print(cnt)
            break