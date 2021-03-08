import sys
from collections import defaultdict
class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.distance = None
        self.parent = None

class Graph:
    def __init__(self,nodes) -> None:
        self.nodes = nodes
        self.adj_list = defaultdict(list)

def addedge(self,u,v):
    self.adj_list[u].append(v)


def initialize_ssp(G,s):
    l = []
    for node in G.nodes:
        newnode = Node(node)
        newnode.distance = sys.maxsize
        
        l.append(newnode)
        s = set()
    return l,s

