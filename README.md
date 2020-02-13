# SearchDuplicateFiles

This is a simple script......

---

### Usage

1. Move the script (getDupFiles.py) to a folder that you want to reduplicate.
2. Simply run
```bash
    python getDupFiles.py
```
3. The script will automatically create the "Duplications" folder in this directory. Then move and rename the duplicate files here.

### 用法
1. 把Python脚本（getDupFiles.py）放到你需要去重的文件夹下（会Python的朋友直接改代码的路径就行）。
2. 直接运行
```bash
    python getDupFiles.py
```
3. 脚本会在本目录新建“Duplications”文件夹，并把重复的文件重命名后放在这里。文件夹名如果需要自定义请自行修改脚本=-=。

### Idea

The idea is simple.
1. Search recursively for all files in the directory.
2. Calculate the MD5 for these files and store in 'Dict'.
3. If "Dict" has this MD5 value, move the file to the default folder ("./Duplications") and rename.

### 设计思路

灰常简单
1. 递归搜索目录中的所有文件。
2. 计算这些文件的MD5并存储在“Dict”中。
3. 如果“Dict”有此MD5值，则将文件移动到默认文件夹(“./ Duplicates”)并重命名。

### Small details that have been considered

1. Large files are read in blocks.
2. Duplicate files move the one with the longer name.
3. Adding a index number to the original name.
4. Do not change suffix names (if any)

### 考虑到的小细节

1. 大文件以块的形式读取。
2. 重复文件移动名称较长的文件。
3. 重命名时，在原来的名称中添加一个数字。
4. 不要更改后缀名(如果有)

### 举个例子Example
```
ORI:
    temp.py
    temp_copy.py
    temp_2.py

After deduplicate......

Retain:
    temp.py
Moved:
    temp_copy2.py
    temp_23.py
```

The end =-=