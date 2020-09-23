# 呆瓜的 Git 學習筆記

> 以防本呆瓜哪天忘記, 在這裡紀錄了一些 git-bash 的使用筆記

## Git
### 由來故事
- 由Linus Torvalds為了管理Linux kernel的開發而開發
- 分散式版本控制軟件
    + 每個人手上都有一份完整的檔案資料 -> 無須中央資料庫
- 僅紀錄檔案的變化 -> 節省檔案的保存空間 
- 授權: GNU GPL

### 架構圖
```
*----------*      *---------*------------*------------------*
| <Remote> |      | <Clone> | <Branches> |  <Working Area>  |
|          |      |         |            |                  |
|        --|------|---------|------------|-> Pull           |
|          |      |       --|-> Reset    |                  |
|          |      |         |          --|-> Checkout       |
|        --|------|-> Fetch |            |                  |
|          |      |         |          --|-> Merge          |
|          |      *---------*            |                  |
|          |      |                      *---------*        |
|          |      |             Commit <-|--     <-|-- Add  |
|          |      |                      | <Stage> |        |
|        <-|------|-- Push               |         |        |
|        <-|------|-- Pull Request       |         |        |
|          |      |                      |         |        |
*----------*      *----------------------*---------*--------*
```

### 筆記
- 初始化, `git init`; 複製下載, `git clone <url>`
- 當要開發新功能, 開一個新的分支, `git branch <name>`
- 切換到新的分支上做事, `git checkout <key>`
- 製作一定程度就提交版本, `git commit -m <msg>`
  + 將檔案變化加入這次要提交的版本, `git add <path>`
- 開發好了, 切回主分支, 將提交合併回分支, `git merge <branch>`
- 同步遠端分支, `git fetch <remote>`

### 指令列表
| 作用 | 指令 |
| :-: | :- |
| 初始化 | `git init` |
| 將檔案加入暫存 | `git add <File>` |
| 將全部檔案加入暫存 | `git add .` |
| 將檔案刪除並加入暫存 | `git rm <File>` |
| 將檔案變更移除暫存 | `git rm --cached <File>` |
| 忽略追蹤特定檔案的變更 | 參見[.gitignore](#.gitignore) |
| 檢視目前工作區狀態 | `git status` |
| 發送版本提交 | `git commit <-m "Massage">` |
| 檢視版本紀錄 | `git log <Commit> <--author=Name> <-p File>` |
| 檢視檔案差異 | `git diff <Commit> <Commit> <File>` |
| 檔案重新命名/搬遷位置 | `git mv <OldPath> <NewPath>` |
| 建立分支 | `git branch <Name>` |
| 切換分支 | `git checkout <Name>` |
| 合併分支 | `git merge <Name>` |
| 刪除分支 | `git branch -d <Name>` |

- 版本相對路徑
    + `HEAD`: 目前版本
    + `HEAD^`: 前一版, `HEAD^^`: 前二版, `HEAD^^^`: 前三版... 
    + `HEAD~N`: 前N版


### .gitignore

設定忽略追蹤特定檔案/檔案類型/資料夾

```git
# 使用 '#' 來撰寫註解
# 忽略追蹤 'hello.c'
hello.c
# 忽略追蹤所有以 '.exe' 為附檔名的檔案
*.exe
# 忽略追蹤 'test' 資料夾與其中的一切
test/
```

- 如果想在不變更`.gitignore`下, 將標註的檔案加入追蹤
    使用 `git add -f <File>`


### .gitattributes

> 暫不明, 呆瓜研究中


## GitHub

恩... 就是個用來交流代碼的網站

### 指令列表

| 作用 | 指令 |
| :-: | :- |
| 新增版本庫位置 | `git remote add <Name> <url>` |
| 複製版本庫至電腦 | `git clone <url>` |
| 將遠端更新下載至電腦 | `git pull <Name>` |
| 將遠端更新同步至電腦 | `git fetch <Name>` |
| 將電腦端更新上傳至遠端 | `git push <Name>` |
