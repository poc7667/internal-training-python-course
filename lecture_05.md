# Python 1o1 - Week 5 - Basic File IO
## Speaker : Poc.hsu
---


# Notice

- [上課資訊公布](http://dqa-dev:1987/poc/python_course/blob/master/announcement.md) 
- [課程討論區在哪裡?](http://cloud-test/) 
- 如何使用 Windows 開發/顯示中文

---

# Install Cygwin
- [Download Cygwin](http://cygwin.com/setup-x86_64.exe)
- 可以讓你顯示中文更便利
- 關於**中文**
	- 請不要在 Windows 命令提示視窗下面嘗試打任何**中文**，成功算你運氣好！
	- 如果真的要輸入中文，還是利用**文字檔**讀入，比較不會有問題
	
---

# Install package - PIP
- Why? 這是一個可以讓你快速安裝任何套件的**套件**。
- 有了它，你就可以大量方便使用其他人寫好的 library
- pip install
- donwload `https://raw.github.com/pypa/pip/master/contrib/get-pip.py`

```python

python get-pip.py
```

---

# install uniout with PIP

- What is uniout for ?

```python
names = ['批歐西']
print names
import uniout
```

- pip install uniout

---

# Review

- Data collection 
	- List
	- Dictionary
- Sort
- 中文處理

---

# Sort of List

- How to sort by column 0 ?
- How to sort by column 1 ?

```python

people =  [
    ["Apple", 500, 1000],
    ["Zebra", 5000,500],
    ["Carlos", 5, 3]
]

sorted(students, key = lambda x : x[0])
sorted(students, key = lambda t : t[2])
sorted(students, key = lambda vivotek : vivotek[1])
```
- Python sort.py

---

# Reverse of List

- L[::-1]
- reversed(L)
- L.reverse()

---




# Open a file

```python

for line in open(<FILE_PATH>, 'r'):
	print line

```

---

# Sanitize strings

- 先看亂七八糟文字範例
- `python open_file_dirty_string.py`
- `' '.join(line.split())`

---

# Sanitize strings

- `' '.join(line.split())`
- 解讀順序
	- line.split() : 先切成list
	- `' '.join` : 把 list 裡面每一個小元素用空白**黏**起來

---

# More split

- split(';')
- split(',')
- 如果要根據多個條件進行 split , [請參考](http://stackoverflow.com/questions/4998629/python-split-string-with-multiple-delimiters)
- Give it a try

	`poc,jack,vivotek,awesome`
	`jimmy;danny;ethan`

---


# Give it a try


```python

python open_file_v2.py
```


---

# Read a TXT file into List


```python

iod_versions = []
for line in open('history.txt'):
	iod_versions.append(line)
```

---

# Write result to file


```python

with open(FILE_PATH, 'w')  as f :
	for version in iod_versions:
		f.write(version)

```

---


# Broswe directory recursively

```python

for root, dirnames, filenames in os.walk('FD8372'):
	...
```

---

# Homework - 1

- 統計各個 module 改版次數

['iod version: <3.0.7.5>',
 'iod version: <3.0.7.4> [M]',
 'iod version: <3.0.7.2>']
 
Output 

	iod:2
	   
---

# Homework - 2

- 計算出 FD8372, IP8362E 到底還有幾個 common bug 沒有解完
- 根據 history.txt 為例，基本上就當做他是正確的吧

		Verify major bug fixed:	<1-184, 186-289,..., 348-351,354,356-361,364-367,370-372,380,382-383,387,392>

預期輸出結果：列出 1~392 裡面，還沒解出來的 Bug 數量

---
		
		
# Homework - 2 

作業資料先以下面的數據做整理

	1-184, 186-289, 291, 294-299, 301-302, 304-305, 307-312, 314-325,327,330-333,335-338,340,343-345,348-351,354,356-361,364-367,370-372,380,382-383,387,392

- 提示: list, range()
 
---

