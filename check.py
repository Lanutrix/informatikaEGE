import requests


dir = '17'
file = int(input())

answ = requests.get(f'https://kpolyakov.spb.ru/school/ege/getanswer.php?egeNo={dir}&topicNo={file}').content.decode()

print(answ)