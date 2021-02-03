# Graph Transpose 
# O(V+E) times
# O(V2) in if using adjacency matrix

from collections import defaultdict
class GraphAbstract:
    def __init__(self,nodes):
        self.nodes = nodes
        self.adj_list = defaultdict(list)

    def addedge(self,u,v):
        self.adj_list[u].append(v)

    def printgraph(self):
        for node in self.nodes:
            print(node,"->",self.adj_list[node])

class GraphTranspose(GraphAbstract):
    pass

class Graph(GraphAbstract):

    def transpose(self):
        graphtranspose = GraphTranspose(self.nodes)
        for node in self.nodes:
            for item in self.adj_list[node]:
                graphtranspose.addedge(item,node)

        return graphtranspose        

            


graph = Graph(["A","B","C","D","E"])
graph.addedge("A","B")
graph.addedge("A","C")
graph.addedge("B","D")
graph.addedge("D","C")
graph.addedge("D","E")
graph.addedge("E","C")
graph.printgraph()
graphtranspose = graph.transpose()
print("\n")
graphtranspose.printgraph()
