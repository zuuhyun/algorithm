from collections import deque
import sys
input = sys.stdin.readline

# 나이트가 이동할 수 있는 8가지 방향
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs():
    queue = deque()
    queue.append((start_x,start_y))
    board[start_x][start_y] = 1
    while queue:
        x, y = queue.popleft()
        if x == end_x and y == end_y:
            return board[x][y] - 1
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= n or nx < 0 or ny >= n or ny < 0:
                continue
            if board[nx][ny] == 0:
                queue.append((nx,ny))
                board[nx][ny] = board[x][y] + 1


T = int(input())
for _ in range(T):
    n = int(input())
    board = [[0]* n for _ in range(n)]
    start_x, start_y = map(int, input().split())
    end_x, end_y = list(map(int, input().split()))
    print(bfs())