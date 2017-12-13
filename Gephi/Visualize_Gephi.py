#!/bin/python
# Visualization 2
# Samuel van Apeldoorn and Mark Rasenberg
# This script must be run in gephi using the console from the
# scripting plugin (see https://github.com/gephi/gephi/wiki/Scripting-Plugin)
# for more information.
# Usage: >>> execFile("~/Visualize_Gephi.py")

import org.gephi.layout.plugin.openord.OpenOrdLayoutBuilder
import org.gephi.layout.plugin.forceAtlas2.ForceAtlas2Builder
import org.gephi.layout.plugin.force.yifanHu.YifanHu
import java.io.StringWriter
import sys
import time

# Path to save the graph files to
# path = 'c:/Users/Samuel/Documents/Dev/masters/SNA/Gephi/'

# # Replace with automatic function.
# annealing_schedules = [
#     [25, 25, 25, 10, 15],
#     [30, 25, 25, 10, 15],
#     [35, 25, 25, 10, 15],
#     [40, 25, 25, 10, 15],
#     [45, 25, 25, 10, 15],
#     [50, 25, 25, 10, 15],
#     [25, 30, 25, 10, 15],
#     [25, 35, 25, 10, 15]
# ]

# def main():
#     for schedule in annealing_schedules:
#         visualize(schedule)

def main():
    for x in range(11):
        vis()

def vis():
    start = time.time()
    layout = org.gephi.layout.plugin.openord.OpenOrdLayoutBuilder().buildLayout()    
    # layout = org.gephi.layout.plugin.forceAtlas2.ForceAtlas2Builder().buildLayout()
    layout.resetPropertiesValues()
    
    # Annealing schedule parameters
    # see https://gephi.org/gephi-toolkit/0.9.1/apidocs/org/gephi/layout/plugin/openord/OpenOrdLayout.html
    # for more parameters.
    # layout.setLiquidStage(s[0])
    # layout.setExpansionStage(s[1])
    # layout.setCooldownStage(s[2])
    # layout.setCrunchStage(s[3])
    # layout.setSimmerStage(s[4])

    LayoutController.setLayout(layout)

    LayoutController.executeLayout() 
    
    # runLayout(org.gephi.layout.plugin.force.yifanHu.YifanHu)

    # Checks whether the previous visualization iterations is finished.
    can_execute = LayoutController.canExecute()
    while not can_execute:
        can_execute = LayoutController.canExecute()
    end = time.time()
    print(end - start)    
    # export_graph(name)


def export_graph(name):
    ec = Lookup.getDefault().lookup(org.gephi.io.exporter.api.ExportController)
    exporter = ec.getExporter('GraphML')
    stringWriter = java.io.StringWriter()
    ec.exportWriter(stringWriter, exporter)
    graph = stringWriter.toString()

    out_file = open(path + name + '.xml', 'w')
    out_file.write(graph)
    out_file.close()


main()