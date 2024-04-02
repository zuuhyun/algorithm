adress = list(input().split(':'))
if adress.count(''):
    while len(adress) > 8:
        del adress[adress.index('')]
    while len(adress) < 8:
        adress.insert(adress.index(''), '0000')

for i in range(8):
    if len(adress[i]) < 4:
        adress[i] = '0' * (4-len(adress[i])) + adress[i]

print(':'.join(adress))