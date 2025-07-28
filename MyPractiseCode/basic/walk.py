import os
print("cwd", os.getcwd())
print("\n")
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print(dirpath,'\n', dirnames,'\n' , filenames)
    print(f'Found directory: {dirpath}')
    for dirname in dirnames:
        print(f'\tSub-directory: {dirname}')
    for filename in filenames:
        print(f'\tFile: {filename}')