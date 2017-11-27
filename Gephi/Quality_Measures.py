#!/bin/python

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import sys

def main(file):
    graph = nx.read_graphml(file)

    # Retrieves the X and Y coordinates for all nodes.
    # consists of dictionaries.
    n_attributes_x = nx.get_node_attributes(graph, 'x')
    n_attributes_y = nx.get_node_attributes(graph, 'y')
    
    length(graph, n_attributes_x, n_attributes_y)

# returns the X and Y coordinate for a specific node
def pos(node, na_x, na_y):
    return na_x[node], na_y[node]


# NOT FINISHED
# Metric for the amount of crossing edges.
# Returns a value between 0 and 1.
def edge_crossings(graph, na_x, na_y):
    edges = nx.number_of_edges(graph)
    c_all = (edges * (edges-1)) / 2
    c_impossible = 0
    for node in n:
        degree = node.degree
        c_impossible += degree * (degree - 1)
    print(c_impossible)


def symmetry(n, m):
    print('Symmetry')


# Edge lenght metrics
def length(graph, na_x, na_y):
    edge_lengths = []

    # calculate length of every edge using pythagorean theorem.
    for edge in nx.edges(graph):
        source = pos(edge[0], na_x, na_y)
        target = pos(edge[1], na_x, na_y)
        length = source[1] - target[1]
        width = source[0] - target[0]
        # a^2 + b^2 = c^2!
        hypothenuse = np.sqrt(length**2 + width**2)
        edge_lengths.append(hypothenuse)

    # print length statistics
    # will be formatted later
    print('Max length:', max(edge_lengths))
    print('Min length:', min(edge_lengths))
    print('Average length:', np.mean(edge_lengths))
    print('Median length:', np.median(edge_lengths))


if __name__ == '__main__':
    main(sys.argv[1])