from os.path import exists

dir = '24'
files = []

for i in files:
    if not exists(f"{dir}\\{i}.py"):
        open(f"{dir}\\{i}.py", 'w').close()
        print(f"Make {dir}\\{i}.py")
