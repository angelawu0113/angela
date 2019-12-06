
# coding: utf-8

# In[5]:


from Cryptodome.Hash import MD5
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyHashSet:
    def __init__(self, capacity = 5):
        self.capacity = capacity
        self.data = [None] * capacity #array
        
    def encryption(self,key): #寫一個負責加密fuction:把字串丟進去，用 MD5 來輸出加密數字，這是參考老師投影片助教給的程式碼
        h = MD5.new()
        h.update(key.encode("utf-8"))
        new_key = int(h.hexdigest(),16)
        return new_key #new_key是加密過的數字
    
    def add(self, key):
        new_key = MyHashSet().encryption(key) #呼叫 encryption()來把 key 加密
        n = new_key % self.capacity #取餘數放到對應的 array index裡
        if self.data[n] == None: # 如果data裡的那個位子是空的，就把 new_key存進去
            self.data[n] = ListNode(new_key)
        else: #如果那個位子已有存東西
            if self.data[n].val != new_key:
                if self.data[n].next == None:#如果 array後面沒有 node，就在他的後面建一個 node
                    self.data[n].next = ListNode(new_key)
                else: # array後面有 node，找到最後一個 node，新增在他後面
                    x = self.data[n] #參考同學的 while走訪概念
                    y = x.next
                    while y.next and y.val != new_key: 
                        y = y.next #現在 y是 linked-list的最後一個 node
                    if y.next == None and y.val != new_key:  
                        y.next = ListNode(new_key)
                
    def remove(self, key):
        new_key = MyHashSet().encryption(key) #呼叫 encryption()來把 key 加密
        n = new_key % self.capacity #取餘數為了放到對應的array index裡
        if self.data[n] != None:
            if self.data[n].val == new_key: #如果要移除的 new_key就在 array裡
                if self.data[n].next != None: # array後面有node，把 array的下一個 node存入array原來的位置
                    self.data[n] = self.data[n].next
                else: # array後面沒有node，直接存成 None
                    self.data[n] = None 
            elif self.data[n].next and self.data[n].val != new_key: #如果後面有 linked-list且array裡的值不適要找的值,就使用 while找到要移除的 new_key
                x = self.data[n] #參考同學的 while走訪概念
                y = x.next
                while y != None and y.val != new_key: 
                    x = y
                    y = y.next #現在 y是那個 new_key， x是 y的前一個 node  
                if y: 
                    x.next = y.next        
        
    def contains(self, key):
        new_key = MyHashSet().encryption(key) #呼叫 encryption()來把 key 加密
        n = new_key % self.capacity #取餘數來決定 key在array的哪裡
        if self.data[n] == None:#如果 array裡的那個位置沒有值
            return False
        elif self.data[n].val != None: #如果 array裡的那個位置有值
            if self.data[n].val == new_key: # key就在 array
                return True
            else: # key不在 array裡
                if self.data[n].next != None: #如果 array後面有 linked-list,使用 while找到key
                    x = self.data[n] #參考同學的 while走訪概念
                    y = x.next
                    while new_key != y.val and y.next:                                
                        y = y.next #現在 y是那個 key， x是 y的前一個 node  
                    if y.val == new_key:
                        return True
                    else: 
                        return False 
                else: # array後面沒有linked-list
                    return False 
                
# 參考資料1：https://docs.google.com/presentation/d/e/2PACX-1vT1HO9Nl475k2bR0l1x8_Tr4V5Wzx0BEqp9bpmHckvj8kTeJehhYVlOJUDVPhLQm6kjGCJ_sLMSBUw5/pub?start=false&loop=false&delayms=3000&slide=id.g7565e27c53_0_20
# 參考資料2：https://github.com/imucici/my-learning-note/blob/master/HW3/binary_search_tree_06170211.py

