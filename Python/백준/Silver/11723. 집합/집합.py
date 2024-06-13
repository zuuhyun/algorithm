import sys
input = sys.stdin.readline
s1 = set()
for _ in range(int(input())):
    cmd_list = list(input().split())
    if len(cmd_list) == 1:
        cmd = cmd_list[0]
    else:
        cmd = cmd_list[0]
        num = int(cmd_list[1])

    if cmd == "add":
        s1.add(num)
    elif cmd == "remove":
        if num in s1:
            s1.remove(num)
    elif cmd == "check":
        if num in s1:
            print(1)
        else:
            print(0)
    elif cmd == "toggle":
        if num in s1:
            s1.remove(num)
        else:
            s1.add(num)
    elif cmd == "all":
        s1 = set(range(1, 21))
    elif cmd == "empty":
        s1.clear()