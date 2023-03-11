from os.path import exists

dir = '25'
files = [i for i in range(127, 131)]

for i in files:
    if not exists(f"{dir}\\{i}.py"):
        open(f"{dir}\\{i}.py", 'w').close()
        print(f"Make {dir}\\{i}.py")
