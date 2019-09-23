# git/github 學習筆記
## 簡介

以防本呆瓜哪天忘記一些操作指令,紀錄了一些關於git/github的操作步驟。

## Git
### 簡介

由Linus Torvalds為了管理Linux kernel的開發而開發。
分散式版本控制軟件,節省檔案空間,無需專用伺服器。

### 基本概念

版本庫<--->(暫存區<--->工作區)
操作原則: 工作好丟暫存區,完成階段開發才放版本庫。
特殊檔案: ".gitignore"管理忽略資料,".gitattributes"管理文件屬性"。

### 指令列表(**全大寫單詞(?)表示需視情況代入**)
#### 基本操作

* 初始化 ```git init```
* 檢視暫存區/工作區狀態 ```git status```
* 工作區--->暫存區 ```git add FILENAME```
* 暫存區--->版本庫 ```git commit -m "MESSENGE" FILENAME```
* 檢視版本庫紀錄 ```git log```

#### 複雜操作

* 偷懶類型
    - 設定預設帳號 ```git config --global user.email "EMAIL"```
    - 設定預設名稱 ```git config --global user.name "Name"```
    - 全彩UI介面 ```git config --global color.ui true```
    - 短指令
        + commit->co ```git config --global alias.co commit```
        + status->st ```git config --global alias.st status```
        + log->lg ```git config --global alias.lg "log --color --graph --all --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit --"```
* 檔案操作
    - 更改名稱\位置 ```git mv OLDFILE NEWFILE```
    - 刪除檔案 ```git rm FILE```
    - 解除追蹤 ```git rm FILE --cached```
* 版本庫相關
    - 檢視版本庫紀錄 ```git log --author="NAME" --grep="SUBCOMSTR" -S "SUBFILESTR" -p FILE```
    - 檢視檔案紀錄 ```git blame -L FROM,TO FILE```
    - 切換版本 ```git checkout NAME```
    - 更改上筆歷史紀錄 ```git commit --amend "MESSENGE"```
    - 取消上筆版本提交 ```git reset ```
    - 查看版本差異 ```git diff OLDVER NEWVER```
        + 相對路徑 ```HEAD^^, HEAD~3```
* 分支
    - 建立分支 ```git branch NAME```
    - 切換節點 ```git checkout NAME```
    - 合併分支 ```git merge NAME```
    - 刪除 ```git branch -d NAME```

### 特殊檔案
#### .gitignore


#### .gitattributes

* 簡介: 管理文件屬性，影響 diff, add, commit, checkout, merge ,...等操作
* [link](./README.md)


## GitHub
### 簡介

恩...就是個用來交流代碼的網站。

### 指令列表(**全大寫單詞(?)表示需視情況代入**)

* 設定位置 ```git remote ORGIN URL```
* 複製版本庫下來 ```git clone URL```
* 更新版本庫
    - 上傳 ```git push ORGIN```
    - 下載 ```git pull ORGIN```

### 免費架站(?)

設定一個名叫gh-pages的分支,進設定調整一下就OK.
僅限定靜態網站。


## 備忘錄

順帶來練習Markdown,git還真是個複雜的工具阿
