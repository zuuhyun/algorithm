n = int(input())
ext = {}

for i in range(n):
    name, extension = input().split(".")
    if ext.get(extension):
        ext[extension] += 1
    else:
        ext[extension] = 1

ext = dict(sorted(ext.items()))

for extension, cnt in ext.items():
    print(extension, cnt)