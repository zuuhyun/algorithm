import sys
input = sys.stdin.readline
for _ in range(int(input())):
    N, M = map(int, input().split())
    docs = list(map(int, input().split()))
    res = 1
    while docs:
        if docs[0] < max(docs):
            docs.append(docs.pop(0))
        else:
            if M == 0:
                break
            docs.pop(0)
            res += 1

        if M > 0:
            M = M - 1
        else:
            M = len(docs) - 1

    print(res)