import unittest
from src.controller.graph_importer import GraphImporter


class GraphImportTest(unittest.TestCase):
    graph = None

    def setUp(self):
        importer = GraphImporter()
        self.graph = importer.build_graph()

    def test_edges_length(self):
        self.assertEqual(len(self.graph.nodes['A'].edges), 3)
        self.assertEqual(len(self.graph.nodes['B'].edges), 1)

    def test_edges_destinations(self):
        node_a_edges = self.graph.nodes['A'].edges
        self.assertIn('B', node_a_edges)
        self.assertIn('D', node_a_edges)
        self.assertIn('E', node_a_edges)
        self.assertNotIn('C', node_a_edges)


if __name__ == "__main__":
    unittest.main()
