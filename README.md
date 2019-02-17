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
### 基礎 \(OuO \)
#### 初始化
``` text
git init
```
#### 檢視暫存狀態
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

## 備忘錄

順帶練習 .md
