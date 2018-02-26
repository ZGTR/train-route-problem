import unittest
from src.controller.graph_importer import GraphImporter
from src.controller.graph_operations import GraphOperations, NO_SUCH_ROUTE


def _split(route):
    return route.split('-')


class GraphImportTest(unittest.TestCase):
    graph = None

    def setUp(self):
        importer = GraphImporter()
        self.graph = importer.build_graph()
        self.graph_operations = GraphOperations(self.graph)

    @unittest.skip
    def test_distances(self):
        self.assertEqual(self.graph_operations.get_distance(_split('A-B-C')), 9)
        self.assertEqual(self.graph_operations.get_distance(_split('A-D')), 5)
        self.assertEqual(self.graph_operations.get_distance(_split('A-D-C')), 13)
        self.assertEqual(self.graph_operations.get_distance(_split('A-E-B-C-D')), 22)
        self.assertEquals(self.graph_operations.get_distance(_split('A-E-D')), NO_SUCH_ROUTE)

    # @unittest.skip
    def test_nr_routes_with_max_stops(self):
        self.assertEqual(len(self.graph_operations.discover_routes('C', 'C', 2, 4)), 2)
        self.assertEqual(len(self.graph_operations.discover_routes('A', 'C', 5, 5)), 3)

    @unittest.skip
    def test_shortest_path(self):
        self.assertEqual(self.graph_operations.shortest_routes('A', 'C'), 9)
        self.assertEqual(self.graph_operations.shortest_routes('B', 'B'), 9)

    @unittest.skip
    def test_nr_routes_with_max_distance(self):
        self.assertEqual(len(self.graph_operations.discover_routes('C', 'C', max_distance=29)), 7)

if __name__ == "__main__":
    unittest.main()
