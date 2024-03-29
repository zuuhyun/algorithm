n = int(input())
ppl = []
tmp = []
for i in range(n):
    value = input()
    if value == 'ENTER':
        ppl.append(tmp)
        tmp = []
    else:
        tmp.append(value)

if len(tmp) > 0:
    ppl.append(tmp)

answer = 0
for p in ppl:
    if len(p) > 0:
        answer += len(set(p))

print(answer)