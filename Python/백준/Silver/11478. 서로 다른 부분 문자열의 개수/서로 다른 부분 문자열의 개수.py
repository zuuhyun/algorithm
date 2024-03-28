words = input()
answer = []
for i in range(len(words)):
    for j in range(i,len(words)+1):
        word = words[i:j]
        if word:
            answer.append(word)

print(len(set(answer)))