import heapq
import sys
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dijkstra():
    heap = []
    heapq.heappush(heap,(board[0][0],0,0))
    dist[0][0] = 0

    while heap:
        cost, x, y = heapq.heappop(heap)
        if x == m - 1 and y == n - 1:
            print(cost)
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= m  or ny >= n:
                continue

            new_cost = cost + board[nx][ny]
            if new_cost < dist[nx][ny]:
                dist[nx][ny] = new_cost
                heapq.heappush(heap,(new_cost,nx,ny))


n, m = map(int,input().split())
board = [list(map(int, input().strip())) for _ in range(m)]
dist = [[1e9]*n for _ in range(m)]

dijkstra()