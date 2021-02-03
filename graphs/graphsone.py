from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.vertexlist = []
        

    def addvertex(self,vertex):
        if vertex in self.vertexlist:
            return "vertex is all ready there !!"
        self.vertexlist.append(vertex)    

    def addedge(self,vertex,edgelist):
        if vertex  in self.vertexlist:
            self.graph[vertex] = edgelist



g = Graph()
g.addvertex('a')
g.addvertex('b')
g.addvertex('c')
g.addvertex('d')
g.addedge('a',['b','d'])
g.addedge('b',['a','c'])
g.addedge('c',['b','d'])
g.addedge('d',['a','c'])
print(g.graph)
