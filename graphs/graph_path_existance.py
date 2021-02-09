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
            print(node,"->",self.adj_list[node])


    def bfs(self,source):
        visited = {}
        for node in self.nodes:
            visited[node]=False
        visited[source] = True    
        queue = []
        queue.append(source)

        while queue:
            queuenode = queue.pop(0)
            # print(queuenode,end=" ")
            yield queuenode
            for adj_vertex in self.adj_list[queuenode]:
                if visited[adj_vertex] == False:
                    visited[adj_vertex] = True
                    queue.append(adj_vertex)





    def dfs_visit(self,source,visited):
        yield source
        for node in self.adj_list[source]:
            if visited[node]==False:
                visited[node]=True
                self.dfs_visit(node,visited)

    def dfs(self,source):
        visited = {}
        for node in self.nodes:
            visited[node] = False

        visited[source] = True

        yield self.dfs_visit(source,visited)    


    def find_path(self,source,destination):
        
        for node in  self.dfs(source):
            # print(node)
            if node == destination:
                return
            print(node,end=" ")    
        

graph = Graph(["A","B","C","D","E","F","G"])
graph.addedge("A","B")
graph.addedge("A","G")
graph.addedge("A","D")
graph.addedge("B","F")
graph.addedge("C","D")
graph.addedge("C","E")
graph.addedge("D","F")
graph.addedge("E","D")
graph.addedge("E","F")
graph.addedge("G","C")
graph.addedge("G","D")
graph.printgraph()
graph.dfs("A")
graph.find_path("A","D")