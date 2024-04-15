from string import ascii_uppercase as alf

f = open('YandexVar3\\24.txt').read()

for i in alf:
    f = f.replace(i,' ')
f = f.split()
f = [int(i) for i in f if int(i)%2==0]
print(max(f))