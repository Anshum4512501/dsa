from collections import defaultdict
class Graph:
    def __init__(self,nodes):
        self.nodes = nodes
        self.adj_list = defaultdict(list)


    def addedge(self,u,v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)


    def printgraph(self):
        for node in self.nodes:
            print(node ,"->",self.adj_list[node])

    def dfsutil(self,visited,source):
        visited[source] = True
        print(source,end=" ")
        for adj_vertex in self.adj_list[source]:
            if visited[adj_vertex] == False:
                
                self.dfsutil(visited,adj_vertex)
               

    def dfs(self,source):
        visited = {}
        for node in self.nodes:
            visited[node] = False

        self.dfsutil(visited,source)           

        



# g = Graph(["A","B","C","D","E","F"])
# g.addedge("A","B")
# g.addedge("A","C")
# g.addedge("A","D")
# g.addedge("B","C")
# # g.addedge("B","D")
# g.addedge("B","E")
# g.addedge("E","A")
# g.addedge("F","E")

g = Graph([1,2,3,4,5,6,7])
g.addedge(1,2)
g.addedge(1,3)
g.addedge(1,4)
g.addedge(2,5)
g.addedge(3,6)
g.addedge(4,7)
g.printgraph()
g.dfs(1)

# g.dfs("A")
                