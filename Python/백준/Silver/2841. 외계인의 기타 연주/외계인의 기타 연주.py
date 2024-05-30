import sys
input = sys.stdin.readline

N, P = map(int, input().split())
melody = []
stack = [[] for _ in range(7)]

cnt = 0
for i in range(N):
    line, pret = map(int, input().split())
    if len(stack[line]) == 0:
        stack[line].append(pret)
        cnt += 1
    else:
        if pret > stack[line][-1]:
            stack[line].append(pret)
            cnt += 1
        elif pret < stack[line][-1]:
            while True:
                if len(stack[line]) == 0 or pret > stack[line][-1]:
                    stack[line].append(pret)
                    cnt += 1
                    break
                elif pret == stack[line][-1]:
                    break
                else:
                    stack[line].pop()
                    cnt += 1

print(cnt)