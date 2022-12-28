
# Dictionary Attack （反混淆字典攻擊系統）
平常在考古一些網站的時候，裡面的js有時候因為作者的一些需求（或者js的個性）還有莫名其妙的擾亂造成其他人無法好好的讀代碼，於是就做了這套python系統一鍵翻譯 至少讓裡面的代碼好讀一點。

此系統針對 https://www.plazmaburst2.com/level_editor/map_edit.php 裡面的 `cached_libs.js?version=xxx` 的混淆系統。

這js裡面有一些行列：  

```
var lil='O0', lIl='2d',lll='right_panel',...
```
 
把那整行丟進dictionary檔，然後用notepad++移除","和開關引號，並且把裡面的一些“=”也替換掉或者讓切割標準換成另一種符號也行（例如“|”，我覺得沒什麼人會用到這個符號），例子如下：

```
var lil|O0, lIl|2d,lll|right_panel,...
```

然後把整個代碼丟進去，再用py檔跑了一下 然後就大功告成了~

## 資料檔案
- 原資料：見 [input.txt](https://github.com/eaglePB2/Py_Dictionary/blob/main/input.txt)  
- 拆出來的查詢：見 [dictionary.txt](https://github.com/eaglePB2/Py_Dictionary/blob/main/dictionary.txt)  
這邊要注意的是，dictionary裡面的字一定要倒著放，這樣才能避免一個很長的單密文被當成多個短的密文導致解密失敗。

## 前置安裝
不需要，有python和手就行

## 效果預覽
見 [output.txt](https://github.com/eaglePB2/Py_Dictionary/blob/main/output.txt)

## 參考文獻
？
