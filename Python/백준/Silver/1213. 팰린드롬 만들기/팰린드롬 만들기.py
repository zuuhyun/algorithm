
name = input()
alp = dict()
for word in name:
    if alp.get(word):
        alp[word] += 1
    else:
        alp[word] = 1

odd_char = ''
keys = sorted(alp.keys())
for key in keys:
    if alp[key] % 2 == 1:
        if odd_char:
            print("I'm Sorry Hansoo")
            exit(0)
        else:
            odd_char = key

answer = ''
tmp = ''
for key in keys:
    cnt = alp[key] // 2
    tmp += key * cnt
answer += tmp

if odd_char:
    answer += odd_char

answer += tmp[::-1]
print(answer)