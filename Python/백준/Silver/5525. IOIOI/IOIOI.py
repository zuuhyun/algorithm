n = int(input())
m = int(input())
s = input()
form = 2*n+1
P = ''
for i in range(1, form+1):
    if i % 2 == 0:
        P += 'O'
    else:
        P += 'I'

answer = 0
for i in range(m):
    if P == s[i:form+i]:
        answer += 1

print(answer)