Algo Dijakshtra 

1. Initialize Single Source Sortest path(G,s)
2. s = None
3. queue = G.v
4. while q is not empty
5.  u = extract_min(q)
6.  s = s union u  
7.  for vertex of G.adj[u]
8.      realax(u,vertex)


