from collections import defaultdict
class Graph:
    def __init__(self,nodes):
        self.nodes = nodes 
        self.adj_list = defaultdict(list)


    def insert(self,u,v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def bfs(self,source):
        visited = {}
        for node in self.nodes:
            visited[node] = False

        queue = []
        visited[source] = True
        queue.append(source)
        while queue:
            queue_node = queue.pop(0)
            print (queue_node, end = " ")
            for node in self.adj_list[queue_node]:
                if visited[node] == False:
                    queue.append(node)
                    visited[node] = True


    def printgraph(self):
        for node in self.nodes:
            print(node,'->',self.adj_list[node])





g = Graph(["A","B","C","D","E","F"])
g.insert("A","B")
g.insert("A","C")
g.insert("A","D")
g.insert("B","C")
g.insert("B","D")
g.insert("B","E")
g.insert("E","A")
g.insert("F","E")

g.printgraph()

g.bfs("A")