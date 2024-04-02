def multi(n):
    for i in range(n, sw_tot+1, n):
        change(i)
def sym(num):
    change(num)
    for i in range(sw_tot//2):
        if num - i < 1 or num + i > sw_tot:
            break
        if switch[num-i] == switch[num+i]:
            change(num-i)
            change(num+i)
        else:
            break
def change(idx):
    if switch[idx] == 1:
        switch[idx] = 0
    else:
        switch[idx] = 1

sw_tot = int(input())
switch = [-1] + list(map(int, input().split()))
st_tot = int(input())

for _ in range(st_tot):
    s, num = map(int, input().split())
    if s == 1:
        multi(num)
    else:
        sym(num)

for i in range(1, sw_tot+1):
    print(switch[i], end = ' ')
    if i % 20 == 0:
        print()