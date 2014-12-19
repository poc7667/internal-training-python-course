# Python 1o1 - Week 4 - Advanced Collection
## Speaker : Poc.hsu
---

# Review

- 記住在 Python 的世界，最基本的變數 **文字** 以及 **數字**
- Data collection 
	- List
	- Dictionary

---


# Homework Review

![inline](https://i.imgur.com/szQiWOp.png)

---


# Homework Review

![inline](https://i.imgur.com/D02RuYG.png)

---


# 偷幹 Ethan 的作業來觀摩

- git clone git@dqa-dev:ethan/python_hw.git
- 如果 ssh 不行，請記得選 http

![inline](https://i.imgur.com/JmlmykB.png)

---


# Version control our files

- git add <FILES>
- git commit -m "<MESSAGE>"
- git push origin master

---

#  03_vvtk_members_drawer.py


```python

#!/usr/bin/python

# -*- coding: utf-8 -*-

from data_transformer import Data as data
# 把 staff list 包成一個 class import 進來
# 這個步驟先跳過別理他。按照原本的方式即可
```

---

# 

```python

drawer = {"中獎者:" : []}
winner_count = 10

for item in xrange(winner_count):

    winner = random.choice(data.vvtk_name_list)

    drawer["中獎者:"].append(winner)

    data.vvtk_name_list.remove(winner)

```

---

# What is a list

![inline](https://i.imgur.com/uvMygJf.png)

---


# What is a list

![inline](https://i.imgur.com/iQfcQe8.png)

---


# What is a list

![inline](https://i.imgur.com/2wjsZ4w.png)

---


# What is a list

- 基本上你不會知道第幾個 index 放著什麼 value
- 只是很單純的把資料，很整齊的放在一個地方，那個地方叫做 `list`
- 擺放資料的順序由你自己決定

---

# What is a list

- 基本上你不會知道第幾個 index 放著什麼 value ?
- eg. 假設全公司名單通通塞入一個 `list`, 
	- 試問 該list index 100 為誰？

---


# Who knows :scream:


---

# Understand dictionary

- 拿出紙筆，畫出兩欄式表格
- 左欄放 **key**
- 右欄放 **value**

---


# Before entering loop

![inline](https://i.imgur.com/a1McbcV.png)

---


# Loop 1
![inline](https://i.imgur.com/Y2xDySN.png)

---

# Loop 2

![inline](https://i.imgur.com/aPqYMPw.png)

---

# Uniq

- Please refer to `uniq.py`


```python

uniq_lst_by_looping = []
for name in raw_name_list:
    if name not in uniq_lst_by_looping:
        uniq_lst_by_looping.append(name)

```

---

# Length of List


```python

raw_name_list = [
    "poc",
    "jimmy",
    "ethan",
]

print len(raw_name_list)

```

---



# Sort of List

- sorted(): return a new sorted list
- sort(): modify the list in-place

---

# Sort of List


```python

students = [
        ['bryant', 'C', 15],
        ['zebra', 'Z', 6],
        ['adam', 'B', 10],
]
```

---


# Sort of List

- How to sort by column 0 ?
- How to sort by column 1 ?

```python

sorted(students, key = lambda x : x[0])

sorted(students, key = lambda x : x[1])
```

- x = ['bryant', 'C', 15]

---

# Reverse of List

- L[::-1]
- reversed(L)
- L.reverse()


---




# Length of Dictionary

```python

names ={
    "good_guys":["danny"],
    "bad_guys":["poc","ethan","victor"]   
}

print len(names)
print len(names.keys())
print len(names["bad_guys"])

```
---

# List to Dictionary

- Hold your pen and write down it on paper
- What is a list
- What is a dictionary

---


# List to Dictionary

- Please see `list_to_dict.py`

---



# More in dictionary

- iteritems()
	- Fetch key, value for each iteration

![inline](https://i.imgur.com/bYWQ43x.png)	

---


# More in dictionary

- keys()

![inline](https://i.imgur.com/Jp7DLu2.png)

---



# 讓我們持續關注~~扁案~~ Ethan 的Code

---


# Homework:family name

---


# Raw data


```python

        ["財務部","A00485","洪秀棻",],
        ["會計部","A00084","邱秀滿",],
        
```

---

# Initial thought

```python

        ["財務部","A00485","洪秀棻"]
        "洪秀棻"
        "洪"
        
```
- key: "洪"
- ~~value: ["財務部","A00485","洪秀棻"]~~
- value: [ ["財務部","A00485","洪秀棻"] ]

---


# Data Structure in your mind


![inline](https://i.imgur.com/IrjRoiG.png)


---

# Homework family name

- 從List找到了**批歐西**


```python

    if family_name not in employee :
        employee[family_name] = [item]
        
```
![inline](https://i.imgur.com/kfRVD3V.png)

---


# Homework family name

- Every thing in Python is **unicode**
- decode : ANYCODE to **unicode**
- encode : **unicode** to ANYCODE



```python

name.decode('utf-8') # from utf8 to unicode
name.decode('utf-8').encode('utf-8') # from unicode to utf8

family_name = name.decode('utf-8')[0:1].encode('utf-8')

```

---



# Homework family name


```python

    if family_name not in employee :
        employee[family_name] = [item]
    else :
        employee[family_name].append(item)

```

---


# Print result


```python

for item in employee :
    print '姓 ',str(item), ' 的總共有 ', str(len(employee[item])), '人'
    
```

---



# Follow the discussion

- http://cloud-test/forum/

![inline](https://i.imgur.com/gCo1ZhO.png)

---




# Assigments - 尾牙抽獎機
- 建議檔名 `03_vvtk_members_drawer.py`
- 從公司隨機抽樣出 10 個員工出來

---


# Assigments - 各部門人數統計 (dictionary)
- 檔名 `03_vvtk_numbers_of_department.py`
- 統計出公司各單位的人數, 直接輸出下面格式即可
	- 進階的同學可以提供使用者輸入介面，讓使用者輸入"組別"，然後查詢結果
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
- 統計出全公司每個人的年資排名
- 進階：提供讓使用者輸入介面
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