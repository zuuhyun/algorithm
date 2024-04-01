tot = int(input())
square = [[0]*100 for _ in range(100)]

for _ in range(tot):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            square[i][j] = 1

answer = 0
for s in square:
    answer += sum(s)
    
print(answer)