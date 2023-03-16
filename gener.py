from os.path import exists

dir = '25'
files = [152,153,159]

for i in files:
    if not exists(f"{dir}\\{i}.py"):
        open(f"{dir}\\{i}.py", 'w').close()
        print(f"Make {dir}\\{i}.py")
