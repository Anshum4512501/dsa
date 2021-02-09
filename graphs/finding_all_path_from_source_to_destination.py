# here we are going to use bfs to find the all path from a given source to destination
from collections import defaultdict
class Graph:
    def __init__(self,nodes):
        self.nodes = nodes
        self.adj_list = defaultdict(list)

    def _are_nodes_exits(self,*args):
        for node in args:
            if node in self.nodes:
                return True

            return False    

    def add_edge(self,source,destination):
        if self._are_nodes_exits(source,destination):

            self.adj_list[source].append(destination)
            self.adj_list[destination].append(source)

    def bfs(self,source):
        visited = {}
        for node in self.nodes:
            visited[node] = False

        visited[source] = True

        queue = []
        queue.append(source)

        while queue:
            quenode = queue.pop(0)
            print(quenode,end=" ")
            for adj_vertex in self.adj_list[quenode]:
                if visited[adj_vertex] == False:
                    queue.append(adj_vertex)
                    visited[adj_vertex] = True



    def printgraph(self):
        for node in self.nodes:
            print(node,"->",self.adj_list[node])


    def find_all_path(self,source,destination):
        visited = {}
        for node in self.nodes:
            visited[node] = False
            



g = Graph(["A","B","C","D","E","F"])
g.add_edge("A","B")
g.add_edge("A","C")
g.add_edge("A","D")
g.add_edge("B","C")
g.add_edge("B","D")
g.add_edge("B","E")
g.add_edge("E","A")
g.add_edge("F","E")

g.printgraph()

g.bfs("A")