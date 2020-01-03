
# coding: utf-8

# In[8]:


from collections import defaultdict 

#Class to represent a graph 
class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
        
    def Dijkstra(self, s): 
        x = {}
        dist = []    #放起點跟各點的距離
        for i in self.graph[s]:  #先把起始點到各點的距離加進去
            dist.append(i)
        n = []  #來放搜索到非 0的數
        path = [s]  #來放走過的點，先放入起始點
        
        while len(path) < len(self.graph):    #後來用 while 才讓 path、dist能一直加數字進去
            
            #先找到最小的數加進 path裡
            for i in range(len(self.graph)):    
                if dist[i] !=0 and i not in path:
                    n.append(dist[i])       
            path.append(dist.index(min(n))) #先在n裡找到最小值 
            n = []      #再清空 n，才不會一直加非 0的數進去
        
        
            #再處理距離的變化
            for i in self.graph[path[-1]]:            
                if i != 0 and self.graph[path[-1]].index(i) not in path:  
                    d = i + dist[path[-1]]
                    if dist[self.graph[path[-1]].index(i)] == 0:   #多一個判斷，如果此點還沒被走過(是0)那就把距離存進去
                        dist[self.graph[path[-1]].index(i)] = d
                    elif d < dist[self.graph[path[-1]].index(i)]: 
                        dist[self.graph[path[-1]].index(i)] = d
        for i in dist:      
            x[str(dist.index(i))] = i 
        
        return x  
    
    def Kruskal(self):
        a = 1
        

        
### 參考資料
#(1) https://www.runoob.com/python/att-list-min.html<br>
#(2) https://blog.csdn.net/lachesis999/article/details/53185299<br>
#(3) https://docs.google.com/presentation/d/e/2PACX-1vTgHO5AkHJS6iN6bnnBMMdHv6E4rabnrC0KwyTRfjad8Ab3IQjbnGvZuQOjDC9t7nKqeroiwcuasJrI/pub?start=false&loop=false&delayms=3000&slide=id.g75dced35f7_0_5
#(4)https://www.youtube.com/watch?v=NLp9C7AvJhk


# In[9]:


g = Graph(9)
g.graph=[[0,4,0,0,0,0,0,8,0],
         [4,0,8,0,0,0,0,11,0],
         [0,8,0,7,0,4,0,0,2],
         [0,0,7,0,9,14,0,0,0],
         [0,0,0,9,0,10,0,0,0],
         [0,0,4,14,10,0,2,0,0],
         [0,0,0,0,0,2,0,1,6],
         [8,11,0,0,0,0,1,0,7],
         [0,0,2,0,0,0,6,7,0]
    
         ];
print("Dijkstra",g.Dijkstra(0))

