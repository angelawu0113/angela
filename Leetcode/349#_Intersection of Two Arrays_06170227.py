
# coding: utf-8

# In[3]:


class Solution:
    def intersection(self, nums1, nums2):
        n = []
        for i in nums1:
            if i in nums2:
                if i not in n:
                    n.append(i)
        return n


# In[4]:


a = [1,2,2,1]
b = [2,3,2]
Solution().intersection(a,b)

