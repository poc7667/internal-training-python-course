# Python 1o1 - Week 1
## Speaker : Poc.hsu
---


# Setup environment

-   Highly Recommended environment OS X, Ubuntu
    -   Windows is not good platform for script language

---

# 準備工具


- 工具一定要先準備好，才能夠讓開發效率，事半功倍
- 比方說如果你的編輯器畫面是白色底，就讓我眼睛很受傷

---

# Python 主程式安裝

- 開發組的 Member 請使用 Python 2.7.x
- 一般的 Member 請使用 Python 3.x 

> 因為公司部門內先前開發的歷史包袱,只能使用 Python 2 

---    

# Python 主程式安裝

-   Windows用戶，記得設定`環境變數`
-   [參考設定文章](https://sites.google.com/a/crayflames.co.cc/crayflames/python/ptp/pythondehuanjingbianshu)
-   [參考設定文章](http://www.foolegg.com/how-to-build-a-python-programming-environment-on-windows/)
-   什麼是環境變數? 讓你整個作業系統都能記住有什麼模組 程式可以用

---    

# Sublime Text 編輯器

- [Sublime Text](http://www.sublimetext.com/3)
-   程式碼不准許有 tab (這是我們課堂的共識)
	-   只允許空白 spaces，記得去調整 editor 的設定

---

# Sublime 設定

- Ctrl+P or Cmd+P , Open Preferences.sublime-settings
- 注意一下該檔案是否有以下的內容即可

```bash 
    // The number of spaces a tab is considered equal to
    "tab_size": 4,

    // Set to true to insert spaces when tab is pressed
    "translate_tabs_to_spaces": true,

```

^		如果你的 Python 是用 tab , 
		容易讓其他的 developer 覺得沒 sense , 水準不夠。
		程式是一項工程，不是藝術。
		重要的是要跟其他的人格式一致，避免造成他人閱讀不易。

---

# Pycharm 
- 也是一款很棒的 IDE 開發工具
- 就自己好好體驗吧，上課將會以 Sublime text 為主

---

# Let's dive into Python World

-   iPython : 互動式 Shell (這是什麼鬼翻譯)
-   反正你可以進入 iPython 這一支程式，在這個環境裡面你可以
	-   快速的撰寫程式碼
	-   更方便看到你寫的內容輸出結果
	-   少打一些字

---
# Hello World in iPython

- 打開命令提示視窗 
- 開始 
- 執行 
- 打入 python (你就可以進入這個領域了！)

~~~python

print "hello world"
print 19870607

~~~	
	
	
- 要離開這個領域，請下 control + c	

---

# Python Script File

- 唉，我在ipython寫完的東西，一離開就沒了

- 但是，其實你可以存檔！

- 建立一個檔案叫做 sample.py (注意附檔名，有的 Windows 會隱藏附檔名)

```bash
#執行你剛剛寫好的程式
python sample.py
```

---
# Variable
-  變數是什麼? What is variable ?
-  一個可以儲存資料的地方
-  程式就是用來處理資料，資料在處理的時候需要有存放的地方
	-  食物在處理的時候，也要有暫時存放的地方 e.g. 鍋子

```Python
#int a = 3 ;
#a=3
a = 3
```

---

# Basic Inputs and outputs



- Output
	- 在視窗上吐出東西
	- 寫入檔案

- Input
	- 從鍵盤接收 input
	- 從檔案接受資料

---


# Output

```Python
print("Hello Poc!")
```

---

# Input

- Receive argument from command line
	- python sample.py 1987 06 07
	
```python
import sys # 去烙人的意思，把 sys 這個人 call 過來 專門負責處理 sys 相關的事情
sys
print(sys.argv)
print(sys.argv[1])
```

---

# Input
- Receive user input in iteractive way
- In Python 2.x
	- please user `raw_input()`

```Python
name = raw_input("Please enter your name:")
```
	In Python 2.x, input() expects something which is a Python expression
	
---

# Conditional Expression - if

```python
name = raw_input("Which is the best company?")
if name=="VIVOTEK":
	print("yes")
```
	
---


# Conditional Expression - if - else

```python
if name=="VIVOTEK":
	print("yes")
else:
	print("go die")
```
	
---

# Conditional Expression - while
```Python

name = raw_input("Which is the best company?")
while name!="VIVOTEK":
   print(name+" is not a good company")
   name = raw_input("Which is the best company?")
```

---

# Debug time

- 為什麼我輸入了 VIVOTEK 還是不能結束跳針

```Python

name = raw_input("Which is the best company?")
while name!="VIVOTEK ":
	name = raw_input("Which is the best company?")
```

---

# Assigments - BMI

```
> 請輸入你的體重: 60
> 請輸入你的身高(公分): 171

	Underweight = <18.5
	Normal weight = 18.5–24.9 
	Overweight = 25–29.9 
	Obesity = BMI of 30 or greater

---