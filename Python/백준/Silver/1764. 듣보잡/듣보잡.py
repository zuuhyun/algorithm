n, m = map(int, input().split())
listen, see = set(), set()

for i in range(n):
    listen.add(input())
for i in range(m):
    see.add(input())

answer = sorted(list(listen & see))
print(len(answer))
for ppl in answer:
    print(ppl)
