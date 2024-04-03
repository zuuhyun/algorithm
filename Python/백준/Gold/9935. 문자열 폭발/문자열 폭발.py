import sys
input = sys.stdin.readline

str = input().strip()
rep = input().strip()
rep_len = len(rep)

stack = []
for i in range(len(str)):
    stack.append(str[i])
    if ''.join(stack[-rep_len:]) == rep:
        for _ in range(rep_len):
            stack.pop()

if stack:
    print(''.join((stack)))
else:
    print('FRULA')