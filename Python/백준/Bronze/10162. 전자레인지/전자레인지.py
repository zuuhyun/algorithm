def time(t, total):
    if total <= 0:
        return 0, total
    count = 0
    count = total // t
    total = total % t
    return count, total

total = int(input())
c3 = 0
c2 = 0
c1 = 0
c3, total = time(300, total)
c2, total = time(60, total)
c1, total = time(10, total)

if total == 0:
    print(str(c3) + " " + str(c2) + " " + str(c1))
else:
    print(-1)