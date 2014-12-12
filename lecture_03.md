# Python 1o1 - Week 3 - Data collection
## Speaker : Poc.hsu
---

# Review last course

- 記住在 Python 的世界，最基本的變數 **文字** 以及 **數字**

---


# Review assignments

![](http://i.imgur.com/miK8ucE.png)


---


# Run others code

- git clone <REPO_PATH>
- git@dqa-dev:alston/python_homework.git

![inline](http://i.imgur.com/kSdZGG3.png)


---


# Outline

- Data collection : list, dictionary
- List 在別的程式語言可能叫做 Array
- Dictionary 在其他地方的外號 hash


---



# List

- 為什麼你要用 List ?
- 因為不會List
	- 你等於不會寫程式
	- 你就不想寫程式

---

# List

- 用量處理大量資料的利器


```python

#想像你今天要儲存一堆人的名字，並且對他做處理
name1 = "Eric"
name2 = "Carlos"
name3 = "Danny"
print name1
print name2
print name3
# 把 Danny 抓出來
if name1 == "Danny":
	print "name 1 contains Danny"
elif name2 == "Danny":
	...

```


---


# List 

```python

names = ["Eric", "Carlos", "Danny"]
for name in names:
	print name

```

---


# List methods

- 新增資料

```python

# insert an element : append
names.append("Poc")
# inset an new list : extend
names.extend(["Poc", "Jimmy"])

```


---


# List methods


```python

#Remove the first matched value
names.remove("poc")
# remove the last item
names.pop()
```

---

# List methods


- 得到第n筆資料

```python

names.index(2)
```

- 反轉 : reverse()

```python

names.reverse()
```

- 排序 : sort()

```python

names.sort()
```

---

# Random select in List
```python

import random

foo = ['a', 'b', 'c', 'd', 'e']

print(random.choice(foo))
```

---


# Dictionary

- 又是好用的資料結構
- LIST : an ordered list of items
- Dictionary (or dict) : for matching some items (called "keys") to other items (called "values").

---


# Dictionary

- Give the **key**
- Find your **value**

![inline fill](http://i.imgur.com/QdMYwwR.png)

---


# Dictionary and List

- LIST : value 可以重複出現
 
![inline fill](http://www.nltk.org/images/maps01.png)

---

# Dictionary and List

- Dictionary : key 絕對不能重複出現

![inline fill](http://i.imgur.com/QdMYwwR.png)

---


# New a dict()

- vvtk_department = dict()
- vvtk_department = {}

---


# Add new item into dict()


```python

vvtk_department["DQA"] = ["Kevin","Ethan","Kurt"]

vvtk_department["RD2"] = ["Diro"]



{'DQA': ['Kevin', 'Ethan', 'Kurt'], 'RD2': ['Diro']}
```

---


# Check for item in dict

- has_key(<KEY>)
- <KEY> in <DICT>


```python

vvtk_department.has_key("RD1")

"RD1" in  vvtk_department

vvtk_department.has_key("RD2")
```

---


# Len in dict


```python

len(vvtk_department)

len(vvtk_department["DQA"])
```

---

# Background for assigments

- 如何把工號轉成數字?
- 'A00354'
- [1:]

---


# Assigments - 尾牙抽獎機
- 作業檔名 `03_vvtk_members_drawer.py`
- 從公司隨機抽樣出 10 個員工出來

---


# Assigments - 各部門人數統計 (dictionary)
- 檔名 `03_vvtk_numbers_of_department.py`
- 統計出公司各單位的人數
- Output(輸出範例)
	- 驗證五組: 10 人
	- 製造組: 30 人
	- ...

---


# Assigments - VIVOTEK 百家姓 (dictionary)
- 作業檔名 `03_vvtk_family_name_static.py`
- 統計出公司裡面每個姓氏的數量個有多少
- Output
	- 許: 20
	- 林: 58

---

# Assigments - How old Are you 
- 檔名 `03_vvtk_how_old_i_am.py`
- 統計出全公司每個人的年資排名，以及找出你自己的順位
- Output(輸出範例)
	- 1 陳文昌
	- 2 藍志忠
	- ...
	- 我是 Poc 排名 689

---



# Referece

- http://larc.ee.nthu.edu.tw/~jcyeh/python/cdoc/tut/tut.html
- http://dowell.colorado.edu/education-python.html
---