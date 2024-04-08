'''
사다리의 개수 와 뱀의 개수 딕셔너리에 저장
주사위를 굴리면서 주사위 굴린 횟수 저장
'''

from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
events = {}

def bfs():
    board = [False] * 101
    dist = [0] * 101

    queue = deque()
    queue.append(1)

    while queue:
        current = queue.popleft()

        for i in range(1,7):
            next_cell = current + i
            if next_cell == 100:
                return dist[current] + 1

            if next_cell in events:
                next_cell = events[next_cell]

            if next_cell <= 100 and not board[next_cell]:
                board[next_cell] = True
                dist[next_cell] = dist[current] + 1
                queue.append(next_cell)


for _ in range(n+m):
    event, move = map(int, input().split())
    events[event] = move

print(bfs())