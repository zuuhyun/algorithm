from itertools import permutations

n, m = map(int, input().split())
num = list(map(int, input().split()))

answer = permutations(num,m)
answer = sorted(set(answer))
for _num in answer:
    print(*_num)