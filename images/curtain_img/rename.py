import os

# 获取当前文件夹中除了rename.py之外的所有文件
files = [f for f in os.listdir('.') if os.path.isfile(f) and f != 'rename.py']

# 对文件列表进行排序
files.sort()

# 重命名文件
for i, filename in enumerate(files, 1):
    os.rename(filename, f"{i}.jpg")
    print(f"Renaming {filename} to {i}.webpg")