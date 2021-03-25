# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 10:24:04 2020

@author: Tina
"""


import pandas as pd
import numpy as np

df = pd.read_excel("MST data.xlsx", header = None).to_numpy()
data = pd.read_excel('MST data.xlsx', index_col = 0)
data = data.values.tolist()
#%%adjacency_matrix
data_ad = np.triu(data)
data_ad  = data_ad.T + data_ad

#%% kruskal
def union(nodes, e): # 加入edge
    if nodes[e[1]] == nodes[e[2]] == 0:
        nodes[e[1]] = nodes[e[2]] = min(e[1], e[2]) + 1
    elif nodes[e[1]] == 0 or nodes[e[2]] == 0:
        nodes[e[1]] = nodes[e[2]] = max(nodes[e[1]], nodes[e[2]])
    else:
        change = max(nodes[e[1]], nodes[e[2]])
        nodes[e[1]] = nodes[e[2]] = min(nodes[e[1]], nodes[e[2]])
        for i in range(len(nodes)):
            if nodes[i] == change:
                nodes[i] = nodes[e[1]]   
    return nodes

def kruskal(all_nodes, edges):
    used_nodes = [0] * (len(all_nodes))
    MST = []
    cost = 0
    while set(used_nodes) != 1 and edges != []:
        element = edges.pop(0)
        if ((used_nodes[element[1]] == used_nodes[element[2]])
                               and (used_nodes[element[1]] != 0 or used_nodes[element[2]] != 0)):
            continue
        
        MST.append(element)
        cost += element[0]
        all_nodes = union(used_nodes, element)
        
    #print(used_nodes)
    return MST, cost

#%% Prim
def Prim(graph):
        distance = [float("inf")] * len(graph)
        parent = [None] * len(graph)
        visit = []
        distance[0] = 0
        parent[0] = 'first'
        for i in range(len(graph)):
            mind = float("inf")
            adding_node = -1
            for j in range(len(graph)):
                if j not in visit and distance[j] < mind:
                    mind = distance[j]
                    adding_node = j
            if adding_node == -1: break
            visit.append(adding_node)
            for k in range(len(graph)):
                if k not in visit and graph[adding_node][k] < distance[k]:
                    distance[k] = graph[adding_node][k]
                    parent[k] = adding_node
                    
        return parent, distance, visit
    
#%% main
nodes = [10, 20, 30, 40, 50]

print('prim')
for n in  nodes :
    dd = data_ad[:n,:n]   
    parent, distance, visit = Prim(dd)
    print(n, "nodes with costs:", sum(distance))

print('\nkruskal')
for n in nodes:
    edges = []
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            edges.append([df[i][j], i - 1, j - 1])
    all_nodes = list(range(1, n + 1))
    edges.sort()
    kruskal_MST, cost = kruskal(all_nodes, edges)
    print(n, "nodes with costs:", int(cost))
    #print(kruskal_MST)





