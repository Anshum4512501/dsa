class Graph:
    def __init__(self,nodes,is_directed = False):
        self.nodes = nodes
        self.is_directed = is_directed
        self.adj_list = {}

        for node in self.nodes:
            self.adj_list[node] = []


    def print_ad_list(self):
        
        for node in self.nodes:
            print(node, "->" ,self.adj_list[node])
    
    def addedge(self,u,v):
        if self.is_directed:

            self.adj_list[u].append(v)
            
        self.adj_list[v].append(u)

# O(E) times to search an edge
    def search_edge(self,source,destination):
        if source in self.nodes:
            if destination in self.adj_list[source]:
                print("Edge found ",source,"->",destination)

            else:
                print("No such edge there",source,"->",destination)
        else:
            print("Ahh!!! Source missing")            

graph = Graph(["A","B","C","D"])
graph.addedge("A","B")
graph.addedge("B","C")
graph.addedge("B","D")

graph.print_ad_list()            
graph.search_edge("B","C")
graph.search_edge("E","E")
