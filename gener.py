from os.path import exists

dir = '17'
files = [i for i in range(135, 144)]

for i in files:
    if not exists(f"{dir}\\{i}.py"):
        open(f"{dir}\\{i}.py", 'w').close()
        print(f"Make {dir}\\{i}.py")
