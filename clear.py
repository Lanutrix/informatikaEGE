import os

d = os.listdir()
for i in d:
    print(i[:3])
    if i[:3]=='24-':
        os.remove(i)