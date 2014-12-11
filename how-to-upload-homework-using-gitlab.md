# Python 1o1 - How to upload homework
## Speaker : Poc.hsu
---


# Why Git

- 快
- 容易 開 branch , 開很大 開不用錢
- 多人分工超容易

---


# 新增專案
- 首先上我們部門的 Gitlab 系統申請帳號
- [Sign up here](http://dqa-dev:1987/users/sign_up)
- 請填寫 gmail 帳號，並且注意垃圾信箱。(其實也可以填寫公司email 一樣要去 MySPAM 裡面收信，超麻煩)
- 註冊之後，點選確認信，就可以登入系統
- 點擊新增專案按鈕
	- ![](https://lh6.googleusercontent.com/K2fIt96bILj9hZJXYTBTQ6e2AWn6sqNuQiA2L95St3ugDo3gFcpThz7SwGwWrjUhTOr2sujBsA=w1892-h607)
- 新增專案
	- ![](https://lh4.googleusercontent.com/okFyzjVddU7QK7dFQbhFMIpB9Ahd2GTJ8vc3ieJCHp4BWm3KHBbE0Rkx1H6E02xeRqXGGl0a_g=w1892-h607)
- 切換到http,複製這串網址
	- ![](https://lh3.googleusercontent.com/TguyaGOdu0NQOLgNGA7xXltHexsyj1OO-VRKtTL_80VxPZGKG_H5owxWu7L84eYU5EnmmSd4gg=w1892-h607)
- 打開 terminal(命令提示字元)，切換到你預定的資料夾
	- `git clone "複製的網址"`
- 這樣就可以把專案 checkout 到你的 local 電腦

---


# 版本控管初體驗
- 假設你在自己電腦的專案資料夾，新增了 `sample.py`
- 查看狀態 `git status`，你會發現你的檔案目前尚未被追蹤
- 假設經過一段時間的工作，現在你想要記錄到目前為止的工作狀態
-  `git add sample.py`
-  `git add some_files`
-  如果你很偷懶可以 `git add ./` 把目前目錄下面所有東西都加入**此次**的版本記錄

- 該增加的檔案都增加了進去之後
- `git commit -m "填入此次的版本記錄的備註"`
- 此時就已完成一次版本記錄

# 還沒結束
- 現在你只是在你的 local PC 完成了版本控管，但是 server 還沒有你的版本記錄
- 此時在你的資料夾下面打上
	- `git push origin master`
	- 就可以把你的版本記錄、以及程式碼檔案通通丟到 Server 做控管。


# 每次要做版本控管就是....
- 當下一次你要在進行版本控管，記得重跑一次 `版本控管初體驗` 的所有流程即可
- 熟了，就很快了！



---


---