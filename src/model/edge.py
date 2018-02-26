

class Edge:
    source = None
    destination = None
    weight = -1

    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = int(weight)
