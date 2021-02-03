from collections import defaultdict
class Graph:
    def __init__(self,nodes):
        self.nodes = nodes
        self.adj_list = defaultdict(list)

    def _are_nodes_exit(self,*args):
        for node in args:
            if node in self.nodes:
                return True
            return False


    def addedge(self,u,v):
        if self._are_nodes_exit(u,v):

            self.adj_list[u].append(v)    

    def printgraph(self):
        for node in self.nodes :
            print(node,"->",self.adj_list[node])


    def find_out_degree(self):
        for node in self.nodes:
            print(node,"->",len(self.adj_list[node]))                


    def in_degree(self):
        for node in self.nodes:
            if node in self.adj_list[node]:
                pass


graph = Graph(["A","B","C","D","E"])
graph.addedge("A","B")
graph.addedge("A","C")
graph.addedge("B","D")
graph.addedge("D","C")
graph.addedge("D","E")
graph.addedge("E","C")
graph.printgraph()

graph.find_out_degree()