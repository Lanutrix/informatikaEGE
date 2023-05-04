import requests


dir = '24'
file = int(input())

answ = requests.get(f'https://kpolyakov.spb.ru/school/ege/getanswer.php?egeNo={dir}&topicNo={file}').content.decode().replace('<br/>', '\n')
print(answ)