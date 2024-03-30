n = int(input())
incar = {}
out = []
answer = 0

for i in range(n):
    incar[input()] = i

for _ in range(n):
    out.append(input())

for i in range(n-1):
    for j in range(i+1,n):
        if incar[out[i]] > incar[out[j]]:
            answer += 1
            break

print(answer)