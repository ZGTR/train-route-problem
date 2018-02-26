import unittest

from src.Exceptions import NodeNameNotExistError
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

    def test_distances(self):
        self.assertEqual(self.graph_operations.get_distance(_split('A-B-C')), 9)
        self.assertEqual(self.graph_operations.get_distance(_split('A-D')), 5)
        self.assertEqual(self.graph_operations.get_distance(_split('A-D-C')), 13)
        self.assertEqual(self.graph_operations.get_distance(_split('A-E-B-C-D')), 22)
        self.assertEquals(self.graph_operations.get_distance(_split('A-E-D')), NO_SUCH_ROUTE)

    def test_nr_routes_with_max_stops(self):
        self.assertEqual(len(self.graph_operations.discover_routes('C', 'C', 1, 3)), 2)
        self.assertEqual(len(self.graph_operations.discover_routes('A', 'C', 4, 4)), 3)

    def test_shortest_path(self):
        self.assertEqual(self.graph_operations.shortest_routes_distance('A', 'C'), 9)
        self.assertEqual(self.graph_operations.shortest_routes_distance('B', 'B'), 9)

    def test_nr_routes_with_max_distance(self):
        self.assertEqual(len(self.graph_operations.discover_routes('C', 'C', max_distance=29)), 7)

    def test_node_name_not_exist_should_cause_exception(self):
        with self.assertRaises(Exception) as ex:
            self.graph_operations.get_distance(_split('A-K'))
        self.assertEquals(ex.exception.message, "A node with a name 'K' doesn't exist")

        with self.assertRaises(Exception) as ex:
            self.graph_operations.get_distance(_split('J'))
        self.assertEquals(ex.exception.message, "A node with a name 'J' doesn't exist")

if __name__ == "__main__":
    unittest.main()
