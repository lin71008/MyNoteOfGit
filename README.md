# git 備忘錄

## 簡介

本人正在練習使用git中...

## 指令列表
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
### 基礎
``` text
git init : 初始化(?)
git status : 檢視暫存狀態
git log : 檢視git樹狀態
git add "FileName" : 追蹤檔案
git add . : 追蹤全部檔案
git commit -m "CommitMessage" "FileName" : 上傳暫存狀態
git mv "OldFileName" "NewFileName" : 改名字/位置
git diff "OldIndex" "NewIndex" : 比較差異
```
## 備忘錄

順帶練習 .md
