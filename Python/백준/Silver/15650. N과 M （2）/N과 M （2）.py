from itertools import combinations
n, m = map(int, input().split())
num_list = [i for i in range(1,n+1)]

answer = combinations(num_list,m)
for num in answer:
    print(*num)