#!/bin/bash

import math

def main():
    nodes = g.nodes
    edges = g.edges

    edge_crossings(nodes, edges)
    length(nodes, edges)


def edge_crossings(n, m):
    len_m = len(m)
    c_all = (len_m * (len_m-1)) / 2
    c_impossible = 0
    for node in n:
        degree = node.degree
        c_impossible += degree * (degree - 1)
    print(c_impossible)


def symmetry(n, m):
    print("Symmetry")


def length(n, m):
    edge_length = []

    for edge in m:
        source = edge.source
        target = edge.target
        length = source.y - target.y
        width = source.x - target.x
        hypothenuse = math.sqrt(length**2 + width**2)
        edge_length.append(hypothenuse)

    print("Max length:", max(edge_length))
    print("Min length:", min(edge_length))
    print("Average length:", sum(edge_length)/len(edge_length))

    if len(edge_length) % 2 == 0:
        print("Median length:", edge_length[len(edge_length)/2])
    else:
        median1 = edge_length[(len(edge_length)/2)-0.5]
        median2 = edge_length[(len(edge_length)/2)+0.5]
        print("Median length:", (median1+median2)/2)

main()