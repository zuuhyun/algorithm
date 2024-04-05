import sys
input = sys.stdin.readline

for _ in range(int(input())):
    clothes = {}
    n = int(input())
    for _ in range(n):
        name, c_type = input().split()
        if clothes.get(c_type):
            clothes[c_type] += 1
        else:
            clothes[c_type] = 1

    reuslt = 1
    for value in clothes.values():
        reuslt *= (value + 1)
        
    print(reuslt-1)