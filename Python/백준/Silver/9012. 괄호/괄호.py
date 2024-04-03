n = int(input())
for _ in range(n):
    str = input()
    if len(str) % 2 == 1 or str[-1] == '(':
        print('NO')
        continue
    stack = []
    answer = ''
    for s in str:
        if s == '(':
            stack.append(s)
        else:
            if stack:
                stack.pop()
            else:
                answer = 'NO'
                break

    if not stack and len(answer) == 0:
        answer = 'YES'
    else:
        answer = 'NO'

    print(answer)