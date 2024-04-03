import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    cmd = input()
    n = int(input())
    num = deque(input().strip()[1:-1].split(','))
    flag = True
    rev = 0
    
    for c in cmd:
        if c == 'R':
            rev += 1
        elif c == 'D':
            #len(deque['']) 는 1
            if n == 0 or len(num) == 0:
                print('error')
                flag = False
                break
            if rev % 2 == 0:
                num.popleft()
            else:
                num.pop()

    if flag:
        if rev % 2 == 0:
            print("[" + ",".join(num) + "]")
        else:
            num.reverse()
            print("[" + ",".join(num) + "]")
