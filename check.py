import requests


dir = '7'

for i in range(132,134):
    answ = requests.get(f'https://kpolyakov.spb.ru/school/ege/getanswer.php?egeNo={dir}&topicNo={i}').content.decode().replace('<br/>', '\n')
    print(answ)