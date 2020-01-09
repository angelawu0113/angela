
# coding: utf-8

# In[13]:


class Solution:
    def uniqueOccurrences(self, arr):
        count = []
        n = []
        for i in arr:
            if i not in n:
                n.append(i)
                count.append(arr.count(i))
        for i in count:
            if count.count(i) != 1:
                return False
        return True
        


# In[14]:


a = [1,2,2,1,1,3]
Solution().uniqueOccurrences(a)

