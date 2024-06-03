import sys
input = sys.stdin.readline

def find_num(A, B):
    cnt = 0
    while B > A:
        if B % 2 == 0:
            B //= 2
        elif B % 10 == 1:
            B //= 10
        else:
            return -1
        cnt += 1

    if B == A:
        return cnt+1
    else:
        return -1

A, B = map(int, input().split())
print(find_num(A,B))