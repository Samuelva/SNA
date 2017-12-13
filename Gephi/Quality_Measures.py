#!/bin/python3
# Visualization II
# Usage: $ python3 Quality_Measures.py graph.GraphML/graph.xml

import matplotlib.pyplot as plt
import math
import networkx as nx
import numpy as np
import sys

def main(file):
    G = nx.read_graphml(file)

    # Retrieves the X and Y coordinates for all nodes.
    # consists of dictionaries.
    n_attributes_x = nx.get_node_attributes(G, 'x')
    n_attributes_y = nx.get_node_attributes(G, 'y')
    
    # edge_crossings(G, n_attributes_x, n_attributes_y)
    avg_length(G, n_attributes_x, n_attributes_y)
    # edge_angle(G, n_attributes_x, n_attributes_y)
    # size(G, n_attributes_x, n_attributes_y)

# returns the X and Y coordinate for a specific node
def pos(node, na_x, na_y):
    return na_x[node], na_y[node]


# Metric for the amount of crossing edges.
# (should) returns a value between 0 and 1.
def edge_crossings(G, na_x, na_y):
    edges = nx.number_of_edges(G)
    c_all = (edges * (edges-1)) / 2
    c_impossible = 0
    for node in n:
        degree = node.degree
        c_impossible += degree * (degree - 1)

    edge_crossings = 0
    crossings = {}

    for edge in G.edges():
        pos_source = pos(edge[0], na_x, na_y)
        pos_target = pos(edge[1], na_x, na_y)

        h_boundary = boundary(pos_source[0], pos_target[0])
        v_boundary = boundary(pos_source[1], pos_target[1])

        for edge2 in G.edges():
            if edge == edge2:
                continue
            pos_source2 = pos(edge2[0], na_x, na_y)
            pos_target2 = pos(edge2[1], na_x, na_y)
            if line_intersection(((pos_source), (pos_target)), (pos_source2, pos_target2)):
                edge_crossings += 1
    
    print(edge_crossings)


def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div != 0:
        return True
    #    raise Exception('lines do not intersect')

    # d = (det(*line1), det(*line2))
    # x = det(d, xdiff) / div
    # y = det(d, ydiff) / div
    # return x, y

# Edge lenght metrics
def avg_length(G, na_x, na_y):
    edge_lengths = []

    # calculate length of every edge using pythagorean theorem.
    for edge in nx.edges(G):
        source = pos(edge[0], na_x, na_y)
        target = pos(edge[1], na_x, na_y)
        length = source[1] - target[1]
        width = source[0] - target[0]
        # a^2 + b^2 = c^2!
        diagonal = np.sqrt(length**2 + width**2)
        edge_lengths.append(diagonal)

    # Outputs average length and standard deviation.
    print(np.mean(edge_lengths), np.std(edge_lengths))


# Determine the length between two node coordinates.
def length(pos_source, pos_target):
    length = pos_source[1] - pos_target[1]
    width = pos_source[0] - pos_target[0]
    return np.sqrt(length**2 + width**2)


# Metric for determining 
def edge_angle(G, na_x, na_y):
    # Ideal minimum angle is calculated to determine at what angle the edges
    # "should" be from each other. Is calculated for every node.
    ideal_min_angles = {degree[0]:360 / degree[1] for degree in nx.degree(G)}

    # Sum of the angular deviation from the ideal angle.
    sum = 0
    # Loop over all nodes to get the angular deviation for every node.
    for node in G.nodes():
        smallest_angle = 360

        # Two loops that loop over the neighbors of node "node", the first loop
        # sets a base edge, against which all other edges coming from node "node" will
        # be compared to determine the angle. Basically, all possible angles between
        # all edges of node "node" are determined, and the smallest is chosen.
        for neighbor1 in nx.all_neighbors(G, node):
            length_AB = length(pos(node, na_x, na_y), pos(neighbor1, na_x, na_y))
            for neighbor2 in nx.all_neighbors(G, node):
                if neighbor1 == neighbor2:
                    continue
                length_AC = length(pos(node, na_x, na_y), pos(neighbor1, na_x, na_y))
                length_BC = length(pos(neighbor1, na_x, na_y), pos(neighbor2, na_x, na_y))

                # Law of cosine to determine the angle between two edges.
                cos_A = (length_AB**2 + length_AC**2 - length_BC**2)/(2*length_AC*length_AB)
                # smallest angle is chosen.
                if np.degrees(np.arccos(cos_A)) < smallest_angle:
                    smallest_angle = np.degrees(np.arccos(cos_A))
                # print('AC', length_AC)
                # print('BC', length_BC)
                # print('AB', length_AB)
                # print('cos_A', cos_A)
                # print('arccos', np.arccos(cos_A))
                # print(np.degrees(np.arccos(cos_A)))
        sum += (ideal_min_angles[node]-smallest_angle)/ideal_min_angles[node]
    
    print((1/nx.number_of_nodes(G)) * sum)


def size(G, na_x, na_y):
    # Upper, left and rightmost and lowest points of the graph.
    max_x = 0
    min_x = 0
    max_y = 0
    min_y = 0

    # Loops over all nodes to determine which nodes are the boundaries.
    for node in G.nodes():
        xy = pos(node, na_x, na_y)
        if xy[0] > max_x:
            max_x = xy[0]
        if xy[0] < min_x:
            min_x = xy[0]
        if xy[1] > max_y:
            max_y = xy[1]
        if xy[1] < min_y:
            min_y = xy[1]
    
    # Calculate surface of the graph like it is an Cartesian grid.
    length = max_y - min_y
    width = max_x - min_x
    print(length*width)


if __name__ == '__main__':
    main(sys.argv[1])