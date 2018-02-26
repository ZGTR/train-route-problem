from src.model.edge import Edge


class Node:
    name = ''
    edges = {}
    is_visited = False

    def __init__(self, name):
        self.name = name
        self.edges = {}

    def add_edge(self, destination, weight):
        self.edges[destination.name] = Edge(self, destination, weight)

    def is_dead_end(self):
        return len(self.edges) == 0
