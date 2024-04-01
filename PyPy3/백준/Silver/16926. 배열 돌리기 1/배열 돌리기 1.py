n, m, r = map(int, input().split())
data = []
for i in range(n):
    data.append(list((input().split())))

for _ in range(r):
    for i in range(min(n,m)//2):
        x,y = i,i
        tmp = data[x][y]

        #하
        for j in range(i + 1, n - i):
            x = j
            prev = data[x][y]
            data[x][y] = tmp
            tmp = prev

        #우
        for j in range(i + 1, m - i):
            y = j
            prev = data[x][y]
            data[x][y] = tmp
            tmp = prev

        #상
        for j in range(i + 1, n - i):
            x = n - j - 1
            prev = data[x][y]
            data[x][y] = tmp
            tmp = prev

        #좌
        for j in range(i + 1, m - i):
            y = m - j - 1
            prev = data[x][y]
            data[x][y] = tmp
            tmp = prev


for value in data:
    print(*value)