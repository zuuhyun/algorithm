from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
ball = deque(enumerate(map(int, input().split())))
answer = []

while ball:
    idx, paper = ball.popleft()
    answer.append(idx+1)

    if paper > 0:
        ball.rotate(-(paper-1))
    else:
        ball.rotate(-paper)

print(*answer)