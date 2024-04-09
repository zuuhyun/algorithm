import sys
input = sys.stdin.readline
stack, op = [], []
count = 1
is_true = True
n = int(input())
for _ in range(n):
    num = int(input())
    while count <= num:
        stack.append(count)
        op.append('+')
        count += 1

    if stack[-1] == num:
        stack.pop()
        op.append('-')
    else:
        is_true = False
        break

if is_true:
    for _op in op:
        print(_op)
else:
    print("NO")