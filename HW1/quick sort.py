
# coding: utf-8

# # Quick Sort
# 
# ## 什麼是Quick Sort?
# 就是一種快速排序，將大問題分成小問題後，再一一解決的方法
# 
# ## 方法：
# 1.設定一個數為基準值，將其他數來跟基準值進行比較<br>
# 2.如果比基準值小，就放在基準值的左邊<br>
# 3.如果比基準值大，就放在基準值的右邊<br>
# 4.將沒有完全排序完的數再重複1、2、3的步驟，直到所有數都被排序完<br>
# 參考資料：http://notepad.yehyeh.net/Content/Algorithm/Sort/Quick/Quick.php
# 
# ## 我的想法：
# 這次作業要做Quick Sort，我是想到可以使用額外的空間來進行排序，首先設定我的基準值為list[0](list的第一個數)，一開始想到可以設定2個空的集合left、right分別來放比基準值小跟比基準值大的數，然後再寫for迴圈讓數值可以重複分成左右2堆，進行排序。
# 
# ### 大概的概念長這樣：
# 1.找基準點，分2群<br>
# 2.小於基準點放左邊的空集合<br>
# 3.大於基準點放右邊的空集合<br>
# 2跟3再回到1寫for迴圈
# 
# ### 還沒想通得部分：
# 那時候還不清楚該怎麼設定基準值，讓基準值設在left跟right的第一個數，以至於在第一次分堆後可以再接續回到第1步驟
# 
# ### 參考網路解法後：
# 後來參考網路上的解法後，找到了同樣使用額外空間的方法，才知道...<br>
# 1.要用def()來定義一個函數，再寫for迴圈才能解決我沒想通的部分<br>
# 2.以及一開始要先設定list的長度，如果list的長度是1或0的話就可以不用排序，直接回傳list<br>
# 參考網址：http://jialin128.pixnet.net/blog/post/142927691-%5B-資料結構-%5D-快速排序法（quick-sort）in-python

# In[8]:


a=[13,43,5,3,9,29]


# In[9]:


#參考網路的解法
def quicksort(list): #使用額外空間
    pivot_list=[]
    left= []
    right= []
    
    if len(list)<=1:
        return list
    
        
    else:
        pivot= list[0] #基準點 pivot 設為 list 第一個數
        for i in list:
            if i > pivot: # i 比 pivot大就在空的 right 裡新增此數
                right.append(i)
            elif i < pivot: # i 比 pivot小就在空的 left 裡新增此數 
                left.append(i)
            else: 
                pivot_list.append(i) 
    return  quicksort(left) + pivot_list + quicksort(right) #回傳比 pivot 小 + pivot + pivot 大的數


# In[10]:


quicksort(a)


# ###自我學習的部分：
# 經過這次作業後我發現我好像不太知道def()函數該怎麼使用，以下是我查完資料後的小筆記...<br>
# 想要定義一個函數，之後只要呼叫就能執行這個函數，可以使用def()這個函數<br>
# 可以用在:<br>
# 1.定義一個"函數"<br>
# def 函數名稱(要處理的參數):<br>
#     打上你所要執行的程式<br>
#     return 要顯示的結果<br>
# 2.定義一個"過程"<br>
# def 函數名稱(要處理的參數):<br>
#     打上你所要執行的程式<br>
# <br>
# 1、2的差異就是有沒有return   
# <br>
# 參考資料：https://ithelp.ithome.com.tw/articles/10187997

# #我的嘗試:
# ##我想嘗試自己寫出原創的QuickSort
# 我的想法是先定義一個bigger的函數和一個smaller函數，分別來處理比pivot大和小的數，最後再定義一個quicksort函數把bigger和smaller合併進行排序

# In[101]:


#定義一個bigger的函數,如果實驗的list有比pivot大就輸出此數
def bigger(list):
    big= []
    pivot= list[0]
    print(pivot) #印出pivot
    for i in list:
        if i>pivot:
            big.append(i)
            print(big) 
        else:
            print(i,"：no bigger than pivot")
    return big


# In[102]:


list=[6,3,8,4,11]


# In[103]:


bigger(list)


# #執行結果：<br>
# 6是pivot<br>
# list[0]是6，沒有大於pivot所以印出no bigger than pivot<br>
# list[1]是3，沒有大於pivot所以印出no bigger than pivot<br>
# list[2]是8，所以在big新增8，印出big=[8]<br>
# list[3]是4，沒有大於pivot所以印出no bigger than pivot<br>
# list[2]是11，所以在big新11，印出big=[8,11]<br>
# 由此可以知道整個迴圈是如何進行的

# In[92]:


#以此類推用同樣的方法定義一個smaller的函數,如果實驗的list有比pivot小就輸出此數
def smaller(list):
    small= []
    pivot= list[0]
    print(pivot) #印出pivot
    for i in list:
        if i<pivot:
            small.append(i)
            print(small) 
        else:
            print(i,"：no smaller than pivot")
    return small


# In[93]:


smaller(list)


# In[57]:


#最後把2個fountion合併，定義一個新的quicksort函數
def quicksort(list):
    pivot= [list[0]]
    if len(list)<=1:
        return list
    else:
        return smaller(list)+pivot+bigger(list)


# In[58]:


quicksort(list)


# In[59]:


#使用不同測值來測試
a=[67,13,6,4,85,3,25,866,0,22]


# In[60]:


quicksort(a)


# #結果發現這樣只排了第一圈，還需要解決剩下的排序

# In[112]:


#於是我再去修改了一次bigger函數，這次多加一個空list來處理else(來放比pivot小的數)
def bigger(list):
    big= []
    other = [] #多設一個空list
    if len(list)<=1:
        return list
    else:
        pivot= list[0]
        for i in list:
            if i>=pivot: #修改成如果list裡的數大於等於基準值就新增此數到 big
                big.append(i)
                print(big) #印出 big來觀察 
            else:
                print(i,"：no bigger than pivot")
                other.append(i)  #用other這個空集合來處理else的數
        return bigger(other)+big


# In[114]:


a=[67,13,6,4,866,85,3,25,0,22]
bigger(a)

