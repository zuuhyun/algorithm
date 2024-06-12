words = input().strip().upper()
word_dic = {}
for word in words:
    if word_dic.get(word):
        word_dic[word] += 1
    else:
        word_dic[word] = 1

answer = []
max_value = max(word_dic.values())
for k,v in word_dic.items():
    if v == max_value:
        answer.append(k)

if len(answer) == 1:
    print(*answer)
else:
    print('?')