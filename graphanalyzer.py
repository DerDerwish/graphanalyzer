#! /usr/bin/python3
# -- coding: utf-8 --

import sys
import json
import networkx as nx
import matplotlib.pyplot as plt
from sys import argv

# function – convert json to graph
def convert_json_to_graph(graph_data, verbose = False):
    G = nx.Graph()
    for node in graph_data['nodes']:
        if node['flags']['client'] == "false" and node['flags']['online'] == "true" :
            if verbose:
                 print("added node: %s", node['id'])
            G.add_node(node['id'])
    for link in graph_data['links']:
#        if link['type'] != 'client' and link['type'] != 'vpn':
        if link['type'] != 'client':
            if verbose:
                 print("added link: %s", link['id'])
            locallink = link['id'].split('-')
            G.add_edge(locallink[0], locallink[1])
    return G

# function – draw the graph
def draw_graph(graph_data):
	nx.draw(graph_data)
	plt.show()

# function – get biggest clique
def get_biggest_clique(graph_data):
    max_clique = []
    for i in graph_data:
        if (len(i) > len(max_clique)): max_clique = i
    return max_clique

# dump test routines
def get_testroutines(graph):
    print("- - BEGIN OF TESTDATA - -")
    print("number of nodes: ",graph.number_of_nodes())
    print("number of edges: ",graph.number_of_edges())
#    print("cliques: ", list(nx.find_cliques(graph)))
    max_clique = get_biggest_clique(list(nx.find_cliques(graph)))
    print("biggest clique: ", len(max_clique), " with ", max_clique)
    print("- - END OF TESTDATA - -")


filename = argv[1]

# print usage
if filename == "--help":
    print("usage: graphanalyzer FILENAME")
    sys.exit(2)

# read file
data = json.load(open(filename, 'r'))

# convert and draw
#draw_graph(convert_json_to_graph(data))
graph = convert_json_to_graph(data)
get_testroutines(graph)
