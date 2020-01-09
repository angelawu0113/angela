
# coding: utf-8

# In[4]:


class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            nums.insert(0,nums.pop(-1))   


# In[6]:


list = [1,2,3,4,5,6,7]
n = 3
Solution().rotate(list,n)
list

