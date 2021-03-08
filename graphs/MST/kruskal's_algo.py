from collections import defaultdict
class Graph:
    def __init__(self,nodes) -> None:
        self.nodes = nodes
        self.adj_list = defaultdict(list)

    def add_edge(self,u,v,w):
        edge = {v:w}
        self.adj_list[u].append(edge)

    def print_graph(self):
        for node in self.nodes:
            print(node,"->",self.adj_list[node])


    def graph_sorted(self):
        self.adj_list = sorted(self.adj_list,key=lambda item: item[0])
        


    def mst(self):
        pass                


g = Graph(["A","B","C","D"])
g.add_edge("A","B",3)
g.add_edge("B","C",5)
g.add_edge("C","D",2)
g.add_edge("D","A",1)
g.graph_sorted()
g.print_graph()
