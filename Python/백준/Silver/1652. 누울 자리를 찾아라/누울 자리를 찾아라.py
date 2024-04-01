n = int(input())
board, answer = [], [0,0]
for _ in range(n):
    board.append(list(input()))

for i in range(n):
    r_cnt, c_cnt = 0, 0
    for j in range(n):
        # row
        if board[i][j] == '.':
            r_cnt += 1
        else:
            r_cnt = 0
        if r_cnt == 2:
            answer[0] += 1

        # col
        if board[j][i] == '.':
            c_cnt += 1
        else:
            c_cnt = 0

        if c_cnt == 2:
            answer[1] += 1

print(*answer)