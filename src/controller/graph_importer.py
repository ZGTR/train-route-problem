import os
import errno
from src.model.graph import Graph

default_path = '../data/graph.txt'


class GraphImporter:
    graph_edges = ''

    def __init__(self, path=default_path):
        this_folder = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(this_folder, default_path)

        with open(my_file, 'r') as content:
            self.graph_repr = content.read()
        graph_repr = self.graph_repr.replace('Graph: ', '')
        self.graph_edges = graph_repr.split(',')

    def build_graph(self):
        graph = Graph()

        for edge in self.graph_edges:
            edge = edge.strip()

            node_source = edge[0]
            node_destination = edge[1]
            edge_weight = edge[2]

            graph.add_edge(node_source, node_destination, edge_weight)

        return graph
