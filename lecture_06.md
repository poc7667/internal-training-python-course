# Python 1o1 - Week 6 - Advanced-File-IO
## Speaker : Poc.hsu
---

# Review
- Install Cygwin
- pip
- open a file
- sanitize strings (`' '.join(ARRAY)`)

---

# Homework - course 05

- 計算出 FD8372, IP8362E 到底還有幾個 common bug 沒有解完
- 根據 history.txt 為例，基本上就當做他是正確的吧

		Verify major bug fixed:	<1-184, 186-289,..., 348-351,354,356-361,364-367,370-372,380,382-383,387,392>

預期輸出結果：列出 1~392 裡面，還沒解出來的 Bug 數量

---
		
		
# Homework - courser 05

作業資料先以下面的數據做整理

	1-184, 186-289, 291, 294-299, 301-302, 304-305, 307-312, 314-325,327,330-333,335-338,340,343-345,348-351,354,356-361,364-367,370-372,380,382-383,387,392

- 提示: list, range()
 
---




# Homework solution

- common bugs

---


# Split by multiple delimiters

delimiters are separated by  **|**

```python

import re
re.split(r'\s |; |, |', line)

```


---

# Clean your folder

![]( https://i.imgur.com/RBPBSMR.png=50x "Title")

---

# Agenda

- clean up your dirty folder
- find target files recursively

---



# Assignment

- 整理**FD8372**資料夾
	- 請到這邊[下載](http://dqa-dev:1987/poc/fd8372)
- 新建資料夾
	- jpg
	- rootfs_change 
	- flashfs_change

---

# Assignment(cont.)	
- 把所有的**圖片檔案**丟到 jpg  資料夾
- 把所有的**.lst**丟到 對應的change 資料夾
	- `FD8372-VVTK-020000_rootfs_md5_2014-08-18_110425.lst` => rootfs_change
   - `FD8372-VVTK-020000_flashfs_2014-08-18_110425.lst` => flashfs_change

---



# Itrate Files/folders recursively

- jump to the file `walk_folder.py`


---


# Get current working Dir


```python

print os.getcwd()

```

---


# Change dir

- Let play it

```python

print os.chdir(path)
```

---




# Create Dir


```python

os.makedirs(directory)
```


---


# Delete Files and folders


```python
os.remove(FILE_PATH) 
os.rmdir(FOLDER_PATH)
```

---


# Copy file


```python

import shutil
shutil.copy2('/dir/file.ext', '/new/dir/newname.ext')
```

---

# Check before creating

	if not os.path.exists(directory):
	    os.makedirs(directory)

---


# Referencece

- [multiple delimiters](http://stackoverflow.com/questions/27397519/python-defining-string-split-delimiter)


---

