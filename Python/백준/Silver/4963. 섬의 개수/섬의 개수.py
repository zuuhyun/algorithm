import sys
input = sys.stdin.readline

dx = [1, -1, 1, -1, 0, 0, 1, -1]
dy = [0, 0, 1, -1 , 1, -1, -1, 1]
def bfs(x,y):
    queue = [(x,y)]
    cnt = 1
    while queue:
        x, y = queue.pop(0)
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if board[nx][ny] == 1:
                board[nx][ny] = 0
                cnt += 1
                queue.append((nx,ny))
    return cnt

while True:
    N,M = map(int, input().split())
    if N == 0 and M == 0:
        break
    board = []
    for _ in range(M):
        board.append(list(map(int, input().split())))

    res = 0
    for x in range(M):
        for y in range(N):
            if board[x][y] == 0:
                continue
            if bfs(x,y) > 0:
                res += 1
    print(res)