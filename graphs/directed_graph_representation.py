from collections import defaultdict
class Graph:
    def __init__(self,nodes,is_directed=False):
        self.nodes = nodes
        self.adj_list = defaultdict(list)
        self.is_directed = is_directed

    def is_node_exist(self,u,v):
        if u in self.nodes and v in self.nodes:
            return True

        return False        
    
    def addedge(self,u,v):
        
        if self.is_node_exist(u,v):
            if not self.is_directed:

                self.adj_list[v].append(u)
            self.adj_list[u].append(v)    
        else:
            print("No such {} node found".format(u))

            
    def printgraph(self):
        for node in self.nodes:
            print(node,"->",self.adj_list[node])


graph = Graph(["A","B","C","D","E"],is_directed=True)

graph.addedge("A","B")
graph.addedge("A","C")
graph.addedge("A","D")
graph.addedge("A","E")
graph.addedge(None,"F")
graph.printgraph()

