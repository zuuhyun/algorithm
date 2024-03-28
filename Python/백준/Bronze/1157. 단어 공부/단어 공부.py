words = input()
words = words.upper()
words_dic = {}
for word in words:
    if words_dic.get(word):
        words_dic[word] += 1
    else:
        words_dic[word] = 1

#리스트 컴프리헨션 사용
answer = [key for key, value in words_dic.items() if max(words_dic.values()) == value]

if len(answer) == 1:
    print(answer[0])
else:
    print('?')