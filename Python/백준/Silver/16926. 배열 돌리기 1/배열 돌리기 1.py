from collections import deque

def rotation():
    for i in range(x, x + row):
        q.append(data[y][i])

    for i in range(y + 1, y + col):
        q.append(data[i][x + row - 1])

    for i in range(x + row - 2, x, -1):
        q.append(data[y + col - 1][i])
        
    for i in range(y + col - 1, y, -1):
        q.append(data[i][x])

    q.rotate(-r) #90도 회전

    for i in range(x, x + row):
        data[y][i] = q.popleft()

    for i in range(y + 1, y + col):
        data[i][x + row - 1] = q.popleft()

    for i in range(x + row - 2, x, -1):
        data[y + col - 1][i] = q.popleft()

    for i in range(y + col - 1, y, -1):
        data[i][x] = q.popleft()


n, m, r = map(int, input().split())
data = []
for i in range(n):
    data.append(list((input().split())))

q = deque()
col = n
row = m
x, y = 0, 0
while True:
    if col == 0 or row == 0:
        break
    rotation()
    y += 1
    x += 1
    col -= 2
    row -= 2

for num in data:
    print(*num)