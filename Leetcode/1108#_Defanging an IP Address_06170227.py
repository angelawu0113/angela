
# coding: utf-8

# In[31]:


class Solution:
    def defangIPaddr(self, address):
        return address.replace(".","[.]")


# In[33]:


n = "1.1.1.1"
Solution().defangIPaddr(n)

