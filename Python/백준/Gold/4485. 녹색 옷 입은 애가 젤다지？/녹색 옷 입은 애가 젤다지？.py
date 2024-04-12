'''
1e9 : 1∗10^9 = 1,000,000,000
-1e9 : −1∗10^9 = -1,000,000,000
'''
import sys
import heapq
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dijkstra():
    heap = []
    heapq.heappush(heap,(board[0][0],0,0))
    dist[0][0] = 0

    while heap:
        cost, x, y = heapq.heappop(heap)
        if x == n - 1 and y == n - 1:
            print(f'Problem {idx}: {cost}')

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            new_cost = cost + board[nx][ny]
            if new_cost < dist[nx][ny]:
                dist[nx][ny] = new_cost
                heapq.heappush(heap,(new_cost,nx,ny))

idx = 1
while True:
    n = int(input())
    if n == 0:
        break

    board = [list(map(int, input().split())) for _ in range(n)]
    dist = [[1e9] * n for _ in range(n)]

    dijkstra()
    idx += 1