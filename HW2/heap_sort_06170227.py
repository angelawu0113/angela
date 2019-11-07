
# coding: utf-8

# In[11]:


class Solution(object):   
    def heap_sort(self, nums):
        """
        :type nums: List[int] ex:[3,2,-4,6,4,2,19],[5,1,1,2,0,0]
        :rtype: List[int] ex:[-4,2,2,3,4,6,19],[0,0,1,1,2,5]
        """
        n=len(nums)
        for i in range(n-1,-1,-1):
            Solution().heapify(nums,n,i)
        for i in range(n-1,0,-1):
            nums[i],nums[0]=nums[0],nums[i]
            Solution().heapify(nums,i,0)
        return nums
    

    def heapify(self,nums,n,i):
        root=i
        left=2*i+1
        right=2*i+2
        if left < n and nums[left] > nums[root]:
            root = left
        if right < n and nums[right] > nums[root] :
            root = right
        if root != i:
            nums[root],nums[i]=nums[i],nums[root]
            Solution().heapify(nums,n,root)


# In[12]:


list=[4,23,5,87,1,34,11]
Solution().heap_sort(list)

