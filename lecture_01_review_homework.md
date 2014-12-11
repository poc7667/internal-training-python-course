# Python 1o1 - Week 1 - Homework
## Speaker : Poc.hsu

---

# Assigments - BMI



> 請輸入你的體重: 60
> 請輸入你的身高(公分): 171

```python

	Underweight = <18.5
	Normal weight = 18.5–24.9 
	Overweight = 25–29.9 
	Obesity = BMI of 30 or greater

```
---

# 常見問題

- 我無法輸入中文或者印出中文會是亂碼
- 原因： ~~誰叫你要用 Windows~~

---


# 編碼問題

-  .py 的內碼為 utf-8 
-  在你的Python 檔案一開頭加上下面這一行
-  如有需要於 windows cmd 輸出非 big5 碼的話，可改用 cygwin 的 python  

```python

# -*- coding: utf-8 -*-
```
---


# 編碼問題結論

- 不要在 Windows Command `命令提示字元` 上面 利用 Python/Ruby/... 跟中文打交道
- 如果非要不可，可以考慮 [cygwin](https://www.cygwin.com/)

^
- 真的要用 Linux 的東西你就買 Mac 或者灌 Ubuntu , CentOS 直接使用
	- 買來的車子如果是 Toyota 就省油的慢慢開，不要土砲想偽裝成法拉利
	- 瞎忙一場，而且還學不到東西。

---

# 常見問題 - 謎樣的 iPython

- `ipython`: 互動介面，你每做一行動作，他就盡可能幫你輸出結果
	- 如何使用 `ipython` ?
	- 好處：快速測試你想得到的結果，類似一個即時練習的遊樂場
	- 壞處：寫作業時，建議千萬別這麼做，上次有人這樣，結果...

---


# 撰寫一份程式檔案

- 開啟一個新檔案，檔名`sample.py` (檔名隨意)
- 存檔之後，執行 `python sample.py` 就可以執行

--- 

# 作業觀摩

```python

weight = float(raw_input("Input your weight:"))
height = float(raw_input("Input your height(cm):"))

count = float(weight/((height*height)/10000))
bmi=round(count,1)

while bmi >=25.0:
    print("Your BMI is "+ str(bmi) + ", you are too fat!")
    break

while 18.5 <= bmi <= 24.9:
    print("Your BMI is "+ str(bmi) + ", you are great!")
    break

while bmi <= 18.4:
    print("Your BMI is "+ str(bmi) + ", you are too skinny!")
    break


```


---