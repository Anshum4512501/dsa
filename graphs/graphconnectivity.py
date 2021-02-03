class Graph:
    def __init__(self,nodes,is_directed = False):
        self.nodes = nodes
        self.adj_list = {}
        self.is_directed = is_directed
        for node in self.nodes:
            self.adj_list[node] = []

    def addedge(self,u,v):
        if self.is_directed:
            self.adj_list[u] = v
        self.adj_list[u] = v

    def printgraph(self):
        for node in self.nodes:
            print(node,"->",self.adj_list[node])
        print("\n")    


g = Graph(["A","B","C","D","E"],is_directed=True) 
g.addedge("A","B")                       
g.addedge("A","C")
g.addedge("B","D")
g.addedge("B","C")
g.printgraph()
graph_undirected = Graph(["A","B","C","D","E"],is_directed=False) 
graph_undirected.addedge("A","B")                       
graph_undirected.addedge("A","C")
graph_undirected.addedge("B","D")
graph_undirected.addedge("B","C")

graph_undirected.printgraph()

