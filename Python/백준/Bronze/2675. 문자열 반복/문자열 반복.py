n = int(input())

for i in range(n):
    cnt, words = input().split()
    for word in words:
        print(int(cnt) * word, end='')
    print('')