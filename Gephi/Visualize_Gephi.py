#!/bin/python
# Visualization 2
# Samuel van Apeldoorn and Mark Rasenberg
# This script must be run in gephi using the console from the
# scripting plugin (see https://github.com/gephi/gephi/wiki/Scripting-Plugin)
# for more information.
# Usage: >>> execFile("~/Visualize_Gephi.py")

import org.gephi.layout.plugin.openord.OpenOrdLayoutBuilder
import java.io.StringWriter

# Path to save the graph files to
path = 'c:/Users/Samuel/Desktop/Graph_'

# Replace with automatic function.
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
    for schedule in annealing_schedules:
        visualize(schedule)


def visualize(s):
    layout = org.gephi.layout.plugin.openord.OpenOrdLayoutBuilder().buildLayout()    
    layout.resetPropertiesValues()
    
    # Annealing schedule parameters
    # see https://gephi.org/gephi-toolkit/0.9.1/apidocs/org/gephi/layout/plugin/openord/OpenOrdLayout.html
    # for more parameters.
    layout.setLiquidStage(s[0])
    layout.setExpansionStage(s[1])
    layout.setCooldownStage(s[2])
    layout.setCrunchStage(s[3])
    layout.setSimmerStage(s[4])

    LayoutController.setLayout(layout)
    can_execute = LayoutController.canExecute()

    # Checks whether the previous visualization iterations is finished.
    while not can_execute:
        can_execute = LayoutController.canExecute()
    LayoutController.executeLayout()       
    
    export_graph(s)


def export_graph(s):
    ec = Lookup.getDefault().lookup(org.gephi.io.exporter.api.ExportController)
    exporter = ec.getExporter('GraphML')
    stringWriter = java.io.StringWriter()
    ec.exportWriter(stringWriter, exporter)
    graph = stringWriter.toString()

    out_file = open(path + '-'.join(str(x) for x in s) + '.xml', 'w')
    out_file.write(graph)
    out_file.close()


main()