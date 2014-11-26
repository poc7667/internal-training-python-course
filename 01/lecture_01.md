# Python 1o1 - Week 1

---


# Setup environment

-   Highly Recommended environment OS X, Ubuntu
    -   Windows is not good platform for script language

---

# 準備工具


- 工具一定要先準備好，才能夠讓開發效率，事半功倍
- 比方說如果你的編輯器畫面是白色底，就請別找我去你電腦前面debug 很傷我眼睛

---

# Python 主程式安裝


    -   建議使用 Python 2, 因為公司部門內歷史的包袱,只能使用 Python 2

    -   Python 2 與 Python 3 基本為不相容，現行許多 libraries 到現在還是只 support Python 2

    -   但是如果你開發程式下定決心就是要在 Windows 平台上面，並且會有大量文字相關(牽扯到怪里怪氣的編碼那麼就用 Python 3)

---    

# Sublime Text

- [Sublime Text](http://www.sublimetext.com/3)
-   程式碼不准許有 tab (這是我們課堂的共識)
	-   只允許空白 spaces，記得去調整 editor 的設定
	    -   OS: 如果你的 Python 是用 tab , 容易讓其他的 developer 覺得沒 sense , 水準不夠。
	    -   程式是一項工程，不是藝術。重要的是要跟其他的人格式一致，避免造成他人閱讀不易。

---
#   Pycharm (Optional)

    -   Windows平台上，整合性很高的 IDE

-   Note:
	-   Windows用戶，記得設定`環境變數`
		-   [參考設定文章](https://sites.google.com/a/crayflames.co.cc/crayflames/python/ptp/pythondehuanjingbianshu)
		-   [參考設定文章](http://www.foolegg.com/how-to-build-a-python-programming-environment-on-windows/)
	-   什麼是環境變數? 讓你整個作業系統都能記住有什麼模組 程式可以用

---

# Hello world to Python


-   Shell: ipython

-   Duck typing 的世界裡面，資料型態只要記住只有 ((數字Number)) 以及 ((文字String))就可以


~~~python

print "hello world"

~~~	
	

---
# Inputs and outputs


-  變數是什麼? What is variable ?

-   Basic I/O

    -   Output

        -   print()

    -   Input

        -   raw\_input()

-   Conditional Expression

    -   if/else

    -   while loop

-   String Concatenation
