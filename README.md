# git/github 學習筆記

## 簡介

以防本呆瓜哪天忘記一些操作指令，紀錄了一些關於git/github的操作步驟。

## Git
### 簡介

分散式版本控制軟件，GPL2, 由Linus Torvalds開發。

### 基本概念
版本庫<--->暫存區<--->工作區
操作原則: 必要才放工作區，工作好丟暫存區， 完成階段開發才放版本庫
特殊檔案: ".gitignore"管理忽略資料, ".gitattributes"管理diff/merge行為

### 指令列表

* 初始化 ```git init```

* 工作區--->暫存區 ```git add FILENAME```
* 暫存區--->工作區 ```git reset FILENAME```
* 檢視暫存區狀態 ```git status```
* 

```

### 初始設定
``` text
git config --global user.email "Your Email"
git config --global user.name "Your Name"
git config --global color.ui true
```
### 偷懶
``` text
git config --global alias.co commit
git config --global alias.st status
git config --global alias.lg "log --color --graph --all --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit --"
```
### 基礎 \\\(OuO \\\)
``` text
git init
```
``` text
git status
```
#### \[新增/移除\]檔案到暫存
``` test
git add "FileName"
git reset "FileName" 
```
#### 更改檔案\[名字/位置\]
``` test
git mv "OldFile" "NewFile" 
```
#### 檢視版本庫狀態
``` text
git log
```
#### 新增檔案到版本庫
``` text
git commit "FileName" -m "Message"
```
#### 查看版本差異
``` text
git diff "OldRevision" "NewRevision"
```
#### 查看舊版本
``` text
git checkout "Revision"
```
#### 回復到舊版本
``` text
git reset "Revision"
git reset --hard "Revision"
```
### GitHub \(/ OwO\)/
#### 設定GitHub位置
``` text
git remote add "Name" "URL"
```
#### 下載GitHub上的版本庫
``` text
git clone "URL"
```
#### \[下載/上傳\]版本庫到GitHub
``` text
git pull "Name"
git push "Name"
```
### 呆瓜 \(///w///\)
#### 分支好難...跳過\(X_X\)

## 備忘錄

順帶來練習Markdown
