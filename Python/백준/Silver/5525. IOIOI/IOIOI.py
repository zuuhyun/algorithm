n = int(input())
m = int(input())
s = input()
answer, cursor, cnt = 0, 0, 0

while cursor < m - 1:
    if s[cursor:cursor+3] == 'IOI':
        cnt += 1
        cursor += 2
        if cnt == n:
            cnt -= 1
            answer += 1
    else:
        cursor += 1
        cnt = 0

print(answer)