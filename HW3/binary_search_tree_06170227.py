
# coding: utf-8

# In[3]:


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
class Solution(object):
    def insert(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode(inserted node)
        """
        if root.val:
            if val <= root.val: #值小於根
                if root.left: #左邊已有值:把此數當成新的根，重複呼叫自己，比根小就新增值在它的左邊
                    Solution().insert(root.left,val)
                else:    #左邊沒值:直接新增為左邊的值
                    root.left = TreeNode(val)
                    return root.left
                
            else: #值大於根
                if root.right:
                    Solution().insert(root.right,val)
                else:   
                    root.right = TreeNode(val)
                    return root.right
        else:
            root.val = val
            return root
            
            
    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(the root of new completed binary search tree) (cannot search())
        """
        new_root = TreeNode(None) #建一個新樹是空的
        Solution().rebuild(root,new_root,target) 
        root = new_root
        return root
    
    def rebuild(self,root,new_root,target):
        if root:
            if root.val != target:
                Solution().insert(new_root,root.val)
            if root.left:
                Solution().rebuild(root.left,new_root,target)
            if root.right:
                Solution().rebuild(root.right,new_root,target)
                
    def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """

        root=root
        if target==root.val:
            return root
        else:
            if target<root.val and root.left:
                if target==root.left.val:
                    return root.left
                else:
                    Solution().search(root.left,target)
            elif target>root.val and root.right:
                if target==root.right.val:
                    return root.right
                else:
                    Solution().search(root.right,target) 
            else:
                return None
                    
            
                    
    def modify(self, root, target, new_val):
        """
        :type root: TreeNode
        :type target: int
        :type new_val: int
        :rtype:TreeNode(the root of new completed binary search tree) (cannot search())
        """
        new_root = TreeNode(None)
        Solution().rebuild_modify(root,new_root,target,new_val)
        root = new_root
        return root
    
    def rebuild_modify(self,root,new_root,target,new_val):
        if root:
            if root.val != target:
                Solution().insert(new_root,root.val)
            else:
                Solution().insert(new_root,new_val)
            if root.left:
                Solution().rebuild_modify(root.left,new_root,target,new_val)    
            if root.right:
                Solution().rebuild_modify(root.right,new_root,target,new_val)

