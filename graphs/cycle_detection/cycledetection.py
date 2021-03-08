from collections import defaultdict
class Graph:
    def __init__(self,nodes) -> None:
        self.nodes = nodes
        self.adj_list = defaultdict(list)

    def add_edge(self,u,v):
        self.adj_list[u] = v

    def find_parent(self,parent,i):
        if parent[i] == -1:
            return i
        if parent[i] != -1:
            return self.find_parent(parent,parent[i])

    def union(self,parent,x,y):
        parent[x] = y             

    def iscycle(self):
        parent = {}
        for node in self.adj_list:
            
            parent[node] = -1

        for item in self.adj_list:
            for node in self.adj_list[item]:
                x = self.find_parent(parent,item)
                y = self.find_parent(parent,node)
                if x== y:
                    return True
                self.union(parent,x,y)

    def print_graph(self):
        for node in self.nodes:
            print(node,"->",self.adj_list[node])

g = Graph(["A","B","C","D"])
g.add_edge("A","B")
g.add_edge("B","C")
g.add_edge("C","D")
# g.add_edge("D","A")
print(g.iscycle())

