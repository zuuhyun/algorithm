x, y = input().split()

len_x, len_y = len(x), len(y)
answer = len_x
for i in range(len_y - len_x + 1):
    tmp = 0
    for j in range(len_x):
        if x[j] != y[i+j]:
            tmp += 1
    answer = min(answer, tmp)

print(answer)
