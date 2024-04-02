def bfs(x,y):
    check = board[x][y]

    for i in range(4):
        cnt = 1
        nx = x + dx[i]
        ny = y + dy[i]

        while 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == check:
            cnt += 1

            if cnt == 5:
                if 0 <= nx + dx[i] < 19 and 0 <= ny + dy[i] < 19 and board[nx + dx[i]][ny + dy[i]] == check:
                    break
                if 0 <= x - dx[i] < 19 and 0 <= y - dy[i] < 19 and board[x - dx[i]][y - dy[i]] == check:
                    break

                print(check)
                print(x+1, y+1)
                exit(0)

            nx += dx[i]
            ny += dy[i]

board = []
for _ in range(19):
    board.append(list(map(int, input().split())))

dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]
for i in range(19):
    for j in range(19):
        if board[i][j] != 0:
            bfs(i,j)

print(0)