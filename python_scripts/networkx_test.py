# -*- coding: utf-8 -*-
"""
Created on Tue Feb 07 08:56:05 2017

@author: mat
"""

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edge(1, 2, weight=4.7)
G.add_edges_from([(3, 4), (4, 5)], color='red')
G.add_edges_from([(1, 2, {'color': 'blue'}), (2, 3, {'weight': 8})])
G[1][2]['weight'] = 4.7
G.edge[1][2]['weight'] = 4
nx.draw(G)
plt.show()

G = nx.Graph()
# G.add_node(1)
# G.add_nodes_from([2,3])
# G.add_edge(1,2)
# e=(2,3)
# G.add_edge(*e)
# G.add_edges_from([(1,2),(2,3)])
#
# H=nx.path_graph(10)
# G.add_nodes_from(H)
#
# G.add_edges_from(H.edges())
#
# nx.write_adjlist(H, 'filetest')
#
# nx.draw(G)
#
# G.remove_edges_from(H.edges())
#
# G.clear()
#
# G.add_edges_from([(1,2),(1,3)])
# G.add_node(1)
# G.add_edge(1,2)
# G.add_node("spam")       # adds node "spam"
# G.add_nodes_from("spam") # adds 4 nodes: 's', 'p', 'a', 'm'
# nx.draw(G)
# plt.show()
#
# edgelist=[(0,1),(1,2),(2,3)]
# H=nx.Graph(edgelist)
#
#
# FG=nx.Graph()
# FG.add_weighted_edges_from([(1,2,0.125),(1,3,0.75),(2,4,1.2),(3,4,0.375)])
# for n,nbrs in FG.adjacency_iter():
#    for nbr,eattr in nbrs.items():
#        data=eattr['weight']
#        if data<0.5: print('(%d, %d, %.3f)' % (n,nbr,data))
#
#
# for (u,v,d) in FG.edges(data='weight'):
#    if d<0.5: print('(%d, %d, %.3f)'%(n,nbr,d))


# test2

# G.add_edge('A', 'B', weight=4)
# G.add_edge('B', 'D', weight=2)
# G.add_edge('A', 'C', weight=3)
# G.add_edge('C', 'D', weight=4)
#
# print(nx.shortest_path(G, 'A', 'D', weight='weight'))
#
# nx.draw(FG)
# nx.draw_spring(FG)
# nx.draw_shell(FG)
# nx.draw_random(FG)
# plt.show()
