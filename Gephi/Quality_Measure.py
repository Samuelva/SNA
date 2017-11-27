#!/bin/bash

import matplotlib.pyplot as plt
import networkx as nx
import sys

def main(file):
    graph = nx.read_graphml(file)

    # Retrieves the X and Y coordinates for all nodes.
    # consists of dictionaries.
    n_attributes_x = nx.get_node_attributes(graph, 'x')
    n_attributes_y = nx.get_node_attributes(graph, 'y')
    

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
    print("Symmetry")


# Edge lenght metrics
def length(graph, na_x, na_y:
    edge_lengths = []

    for edge in nx.edges(graph):
        source = pos(edge[0], na_x, na_y)
        target = pos(edge[1], na_x, na_y)
        length = source[1] - target[1]
        width = source[0] - target[0]
        # Length of an edge. Is calculated using Pythagorean theorem.
        hypothenuse = math.sqrt(length**2 + width**2)
        edge_lengths.append(hypothenuse)

    print("Max length:", max(edge_lengths))
    print("Min length:", min(edge_lengths))
    print("Average length:", sum(edge_lengths)/len(edge_lengths))

    if len(edge_lengths) % 2 == 0:
        print("Median length:", edge_lengths[len(edge_lengths)/2])
    else:
        # If there are 2 median values
        median1 = edge_lengths[int((len(edge_lengths)/2)-0.5)]
        median2 = edge_lengths[int((len(edge_lengths)/2)+0.5)]
        print("Median length:", (median1+median2)/2)

main()