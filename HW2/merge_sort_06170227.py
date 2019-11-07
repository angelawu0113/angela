
# coding: utf-8

# In[4]:


class Solution(object): #首先定義一個分割陣列的涵式
    def merge_sort(self,nums):
        """
        :type nums: List[int] ex:[3,2,-4,6,4,2,19],[5,1,1,2,0,0]
        :rtype: List[int] ex:[-4,2,2,3,4,6,19],[0,0,1,1,2,5]
        """
        left=[]
        right=[]
        middle=len(nums)//2 #定義中間數的index
        if len(nums)<=1: #如果陣列長度是0、1就可以不用分割，直接回傳此陣列
            return nums
        else:   #陣列長度大於1，進行分割
            for n in nums[0:middle]:  #將middle以前的數新增到left
                left.append(n)
            for n in nums[middle:]:  #從middle以後的數新增到right
                right.append(n) 
            left=Solution().merge_sort(left)  #重複呼叫pile涵數來處裡分割，直到分到只剩一個元素
            right=Solution().merge_sort(right)
        return Solution().sort(left,right) #後來才知道要呼叫 class裡的其他 function要用 MergeSort().sort()，不然程式碼執行時會以為sort()是外面定義的function
                       
    def sort(self,left,right): #再進行排序 
        M=[] 
        i=0 
        j=0
        #一開始用 for迴圈讓整個排序可以執行整個陣列的次數
        for n in range(len(left)+len(right)):
            #如果left裡數的index超出整個 list的長度，就代表left裡的數都比完放進M裡
            #只剩right裡還有數，那就把 right裡剩下的數全部新增到 M
            
            if i>len(left)-1:
                for y in right[j:]: 
                    M.append(y)
                break   #我後來發現要用break來停止這個迴圈，不然會重複新增數到 M裡
                
            elif j>len(right)-1:
                for x in left[i:]:
                    M.append(x)
                break              
            elif (left[i]<=right[j]):
                M.append(left[i])
                i+=1         
            elif (left[i]>right[j]):
                M.append(right[j])
                j+=1          
     
        return M


# In[5]:


list=[4,24,142,75,2,0,24,7] #測試結果：成功排序，完成 merge sort
Solution().merge_sort(list)

