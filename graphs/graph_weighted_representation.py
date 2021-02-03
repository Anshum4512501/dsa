class Graph:
    def __init__(self,nodes):
        self.nodes = nodes
        self.adj_list = {}
        for node in self.nodes:
            self.adj_list[node] = {}


    def insert_into_graph(self,u,v,w):

        self.adj_list[u][v] = w
        self.adj_list[v][u] = w 

    def print_graph(self):
        for node in self.nodes:
            print(node,"->",self.adj_list[node])


g = Graph(["A","B","C","D","E"])
g.insert_into_graph("A","B",4)
g.insert_into_graph("A","C",5)
g.print_graph()                    