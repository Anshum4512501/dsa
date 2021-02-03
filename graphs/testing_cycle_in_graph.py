# detecting cycle in directed graph
from collections import defaultdict
class Directed_Graph:
    def __init__(self,nodes):
        self.nodes = nodes 
        self.adj_list = defaultdict(list)

    def _are_nodes_exist(self,*nodes):
        for node in nodes:

            if node not in self.nodes:
                print("No such node {}".format(node))    
                return False
        return True        

    def addedge(self,u,v):
        if self._are_nodes_exist(u,v):
            self.adj_list[u].append(v)

    def testing_cycle(self):
        pass
    

    def dfsvisit(self,source,visited):
        print(source,end=" ")
        for node in self.adj_list[source]:
            if visited[node]==False:
                visited[node] = True
                self.dfsvisit(node,visited)
        

    def dfs(self,source):
        if self._are_nodes_exist(source):
            visited = defaultdict(lambda:"defalut")

            for node in self.nodes:
                visited[node]=False
            visited[source] = True
            self.dfsvisit(source,visited)    


    def printgraph(self):
        for node in self.nodes:
            print(node,"->",self.adj_list[node])




graph = Directed_Graph(["A","B","C","D","E"])

graph.addedge("A","B")
graph.addedge("A","C")
graph.addedge("B","C")
graph.addedge("B","D")
graph.addedge("C","D")
graph.addedge("C","E")
graph.addedge("D","E")

graph.printgraph()

graph.dfs("A")