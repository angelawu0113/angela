
# coding: utf-8

# In[2]:


from collections import defaultdict 
class Graph:
    
    def __init__(self): 
        self.graph = defaultdict(list) 

    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    def BFS(self, s): 
        node1 = [s]
        queue = []
        for n in self.graph[s]:
            queue.append(n)
        
        for i in range(len(self.graph)-1):
            if queue[i] != None:
                node1.append(queue[i])
                for j in self.graph[queue[i]]:
                    if j not in queue:
                        if j not in node1:
                            queue.append(j)
        return node1
    
    def DFS(self, s):
        node2 = [s]
        stack = []
        for n in self.graph[s]:
            stack.append(n)
        
        for x in range(len(self.graph)-1):
            if stack[-1] != None:
                node2.append(stack.pop(-1))
                for y in self.graph[node2[-1]]:
                    if y not in stack:
                        if y not in node2:
                            stack.append(y)
        return node2
    
#參考資料：
#if in 用法：https://www.jianshu.com/p/0a17e1d1e753
#BFS、DFS概念：https://docs.google.com/presentation/d/e/2PACX-1vTma_vOZyE70O23KWw4I4Y78aAaT5fJSTq7Mae912kCwka_u5ZMWPoo14D86-x-57kZPbb6hAGktSW4/pub?start=false&loop=false&delayms=3000&slide=id.g7a5d8b85ee_0_23

