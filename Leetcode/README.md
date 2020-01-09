# 學習筆記
### 題目：709 To Lower Case <br>
目的：將所有輸入的字串都轉為英文小寫輸出<br>
str.upper()          #把所有字符中的小寫字母轉換成大寫字母<br>
str.lower()          #把所有字符中的大寫字母轉換成小寫字母<br>
str.capitalize()     #把第一個字母轉換為大寫字母，其餘小寫<br>
str.title()          #把每個單字的第一個字母轉換為大写，其餘小寫<br>
參考資料：https://www.runoob.com/python3/python3-upper-lower.html<br>
### 題目：349 Intersection of Two Arrays<br>
目的：輸入2個array，輸出都有在2個 array裡面的值<br>
用for迴圈跟if in 來判斷有沒有同樣的值<br>
### 題目：1207 Unique Number of Occurrences
目的：輸入一組整數數字，當每個數在list裡出現的次數是唯一的時候回傳True，不是唯一就回傳False<br>
list.count(obj)    #計算obj在list裡的出現次數
### 題目：189 Rotate Array
目的：輸入一組list跟一個數字(n)，取出最後一個數字放到最前面成為新的list，然後再重複執行n次，最後輸出改過的list
用for i in range(要執行的次數)，然後用.pop()取出最後一個數，再用.insert()插入在最前面



