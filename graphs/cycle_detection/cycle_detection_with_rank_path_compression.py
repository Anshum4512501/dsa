from collections import defaultdict
class Subset:
    def __init__(self,parent) -> None:
        self.parent = parent
        self.rank = 0

class Graph:
    def __init__(self,nodes) -> None:
        self.nodes = nodes
        self.adj_list = defaultdict(list)

    def find_operation(self,u):
        if u.parent ==u:
            return u
            
        return self.find_operation(u.parent)
        

    def union_operation(self,u,v):
        pass

    def add_edge(self,u,v):
        self.adj_list[u].append(v)

    def is_cycle(self):

        return True        