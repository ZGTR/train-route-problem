from src.model.node import Node


class Graph:
    nodes = {}

    def __init__(self):
        return

    def add_edge(self, source, destination, weight):
        self.add_node(source)
        self.add_node(destination)
        self.nodes[source].add_edge(self.nodes[destination], weight)

    def add_node(self, name):
        if name not in self.nodes:
            self.nodes[name] = Node(name)
