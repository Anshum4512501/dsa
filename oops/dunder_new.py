# Finding dfs of a graph 
from collections import defaultdict
class Graph:
    def __init__(self,nodes):
        self.nodes = nodes
        self.adj_list = defaultdict(list)

    def add_edge(self,source,destination):
        self.adj_list[source].append(destination) 
        self.adj_list[destination].append(source) 

    def printgraph(self):
        for node in self.nodes:
            print(node,"->",self.adj_list[node])

    def dfs(self,source):
        visited = {}
        for node in self.nodes:
            visited[node] = True

        visited[source] = True

    def dfs_visit(self,source,visited):

        for adj_vertex in self.adj_list[source]:
            print(adj_vertex,end=" ")
            if visited[adj_vertex] == False:
                visited[adj_vertex] = True
                self.dfs_visit(adj_vertex,visited)


graph = Graph(["A","B","C","D","E"])
graph.add_edge("A","B")
graph.add_edge("A","C")
graph.add_edge("A","D") 

graph.printgraph()

graph.dfs("A")