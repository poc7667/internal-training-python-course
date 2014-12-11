# Python 1o1 - Week 2
## Speaker : Poc.hsu
---

# Outline
- Advanced control flow
- Basic data type : string, float, integer
- 記住在 Python 的世界，最基本的變數
	- 不是 `文字` 就是 `數字`
	- 先不論 True, False, boolean 變數

---

# String
- 大家都說 Python 處理字串非常強大
- 記得字串記得用 單引號 或者 雙引號 括弧起來
- name = poc
- name = "poc"
- name = 'poc'

--- 


# More about string

- upper/lower

```python

>>> company="vIvoTEk"
>>> company.upper()
'VIVOTEK'
>>> company.lower()
'vivotek'
```

---


# More about string

- contains

```python
>>> "vivo" in company.lower()
True
>>> "iivivo" in company.lower()
False
```
---


# More about string

- concatenation

```python
>>> company + 2014
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: cannot concatenate 'str' and 'int' objects

>>> company + str(2014)
'vIvoTEk2014'
```
---

# More about string

- 讓使用者輸入
	- 年齡：50
	- 姓名：更生人
	- 地區：台北市

輸入完之後，輸出

- 安安你好！我是 "更生人" 住在 "台北市" 今年 "50" 歲， 你呢?

- 動手做做看 3 分鐘

---	


# More about string

- Variables escape from string


```python
>>> name='更生人'
>>> age=50
>>> location = "台北"
>>> print "安安你好！我是 {0} 住在 {2}  今年 {1} 歲， 你呢?"
          .format(name, location, age)
```  


---

# Number

- 下面的適合於 iPyhton 實驗

```python

salary = 100
print (salary*5)
ss = str(salary)
weight = 59.1
5/2
5.0/2
5/float(2)
money = '50'
int(money)
float(money)
```
---

# Conditional if/else

```python

    if a > 5:
        print (a,">",5)
    elif a <= 7:
        print (a,"<=",7)
    else:
        print ("Neither test was true")
```

---



# 作業觀摩

```python
weight = float(raw_input("Input your weight:"))
height = float(raw_input("Input your height(cm):"))
count = float(weight/((height*height)/10000))

bmi=round(count,1)
```

---

# 作業觀摩

```python
while bmi >=25.0:
    print("Your BMI is "+ str(bmi) + ", you are too fat!")
    break

while 18.5 <= bmi <= 24.9:
    print("Your BMI is "+ str(bmi) + ", you are great!")
    break
```


---

# Conditional if/else add while in


```python

a = 0
while a < 10:
    a = a + 1
    if a > 5:
        print (a,">",5)
    elif a <= 7:
        print (a,"<=",7)
    else:
        print ("Neither test was true")

```

- 實例 : 偵測 Camera 是否 alive？ 如果 retry  超過一定次數沒有回應 就判定 ooxx

---

# Quiz

- 來一個階乘 10!
- 什麼是階乘 ??
- E.g.  
	- 3! = 3 x 2 x 1
	- 10! = 10 x 9 x ... x 1

---


# Where is FOR loop ?

- 傳說中的 For loop 該怎麼用 ?

```c
    int i=0;
    for( i = 0 ; i<10 ; i++)
    {
        printf("%d", i);
    }
```

---

# FOR loop Python version

```python
for i in range(99):
	print i
	
for i in range(1,10,3):
	print i
```

---


# Assigments - BMR
- 作業檔名 `02_bmr.py`

- 計算基礎代謝率 
- input ： 體重、性別、身高、年齡
- output：每天最低身體消耗熱量

```
BMR(男)=(13.7×體重(公斤))+(5.0×身高(公分))-(6.8×年齡)+66
BMR(女)=(9.6×體重(公斤))+(1.8×身高(公分))-(4.7×年齡)+655

```

---


# Assigments - 九九乘法加倍奉還版
- 作業檔名 `02_multiplies.py`
- output：印出 99x99 乘法表 table

```
1x1=1
1x2=2
...
99x98=..
99x99=..

```

---

# Assigments - 終極密碼猜數字
- 作業檔名 `02_guess_number.py`


```
>> 請猜密碼，範圍  1~100
>> 13
>> 請猜密碼，範圍  13~100
>> 50
>> 請猜密碼，範圍  13~50
>> 38
>> 恭喜你猜中了，猜了7次

```

---