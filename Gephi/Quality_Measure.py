#!/bin/bash

import math
import org.gephi.layout.plugin.openord.OpenOrdLayoutBuilder


annealing_schedules = [
    [25, 25, 25, 10, 15],
    [30, 25, 25, 10, 15],
    [35, 25, 25, 10, 15],
    [40, 25, 25, 10, 15],
    [45, 25, 25, 10, 15],
    [50, 25, 25, 10, 15],
    [25, 30, 25, 10, 15],
    [25, 35, 25, 10, 15]
]

def main():
    nodes = g.nodes
    edges = g.edges

    for schedule in annealing_schedules:
        layout = org.gephi.layout.plugin.openord.OpenOrdLayoutBuilder().buildLayout()    
        init_layout(schedule)
        edge_crossings(nodes, edges)
        length(nodes, edges)


def init_layout(s):
    go = layout.canAlgo()
    while go == False:
        go = layout.canAlgo()

    layout.resetPropertiesValues()
    layout.setLiquidStage(s[0])
    layout.setExpansionStage(s[1])
    layout.setCooldownStage(s[2])
    layout.setCrunchStage(s[3])
    layout.setSimmerStage(s[4])
    LayoutController.setLayout(layout)
    LayoutController.executeLayout()

    layout.endAlgo()

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
        median1 = edge_length[int((len(edge_length)/2)-0.5)]
        median2 = edge_length[int((len(edge_length)/2)+0.5)]
        print("Median length:", (median1+median2)/2)

main()