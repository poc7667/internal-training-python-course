Week 1
======

Why Learning programing?
------------------------

-   Higher salary ?

-   Easy to find job ?

Why Python ?
------------

-   [程式語言排名][1]

    [1]: <http://www.tiobe.com/index.php/content/paperinfo/tpci/index.html>

-   Python 7th position

-   那幹嘛不學第一名的 C

    -   其實你整本C看完，你做不了什麼應用的案例出來

    -   你會發現要完成一個功能，要大費周章

    -   更多時候你會發現，你在意的不是執行時間

        -   1ms 跟 0.01ms 在大多數的應用，你不會感受到差異。

        -   但是不同程式語言開發速度帶來的差異，就會讓你很有感。

    -   C語言大多就是擔任底層系統工程師的任務為主

Basic
=====

Setup your own environment
--------------------------

-   Most recommend environment OS X, Ubuntu

    -   Windows is not good platform for script language

### Things you need to donwload

-   [Python][2]

    [2]: <https://www.python.org/downloads/>

    -   建議使用 Python 2, 因為部門內歷史的包袱,只能使用 Python 2

    -   Python 2 與 Python 3 基本為不相容，大量的 libraries 到現在還是只support Python 2

    -   但是如果你開發程式下定決心就是要在 Windows 平台上面，並且會有大量文字相關(牽扯到怪里怪氣的編碼那麼就用 Python 3)

-   [Sublime Text][3]

    [3]: <http://www.sublimetext.com/3>

    -   程式碼不准許有tab，只允許空白 spaces，記得去調整 editor 的設定

-   Pycharm

    -   Windows平台上，整合性很高的 smart IDE

-   Note:

    -   **Windows用戶，記得要把環境變數設定上去**

    -   **什麼是環境變數? 讓你整個作業系統都能記住有什麼模組/程式可以用**

Hello world to Python
---------------------

-   Shell: ipython

-   Duck typing 的世界裡面，資料型態只要記住只有 ((數字Number)) 以及 ((文字String))就可以

Inputs and outputs
------------------

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
