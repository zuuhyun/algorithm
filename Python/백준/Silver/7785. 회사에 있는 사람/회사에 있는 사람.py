n = int(input())
ppl = {}

for i in range(n):
    name, status = input().split()
    if ppl.get(name) and status == 'leave':
        del ppl[name]
    else:
        ppl[name] = status

answer = list(ppl.keys())
answer.sort()
answer = answer[::-1]
for worker in answer:
    print(worker)