import os
import sys
from src.exceptions.NodeNameNotExistError import NodeNameNotExistError
from src.model.graph import Graph

NO_SUCH_ROUTE = 'NO SUCH ROUTE'

class GraphOperations:
    graph = None

    def __init__(self, graph):
        self.graph = graph

    def _clean_is_visited(self):
        for key, node in self.graph.nodes.items():
            node.is_visited = False

    def _validate_nodes_names(self, nodes_names_list):
        for name in nodes_names_list:
            # If the node not in the graph nodes, raise an exception
            if name not in self.graph.nodes:
                raise NodeNameNotExistError("A node with a name '{0}' doesn't exist".format(name))

    def get_distance(self, nodes_names_list):
        self._validate_nodes_names(nodes_names_list)

        nodes_list = []
        for name in nodes_names_list:
            # If the node not in the graph nodes, raise an exception
            if name not in self.graph.nodes:
                return NO_SUCH_ROUTE
            nodes_list.append(self.graph.nodes[name])
        return self._get_distance(nodes_list)

    def _get_distance(self, nodes_list):
        if len(nodes_list) == 0:
            return -1

        distance = 0
        scanner = 1

        current_node = nodes_list[0]

        while scanner < len(nodes_list):
            next_node = nodes_list[scanner]
            if next_node.name not in current_node.edges:
                return NO_SUCH_ROUTE
            current_edge = current_node.edges[next_node.name]
            distance += current_edge.weight
            current_node = current_edge.destination
            scanner += 1

        return distance

    def shortest_routes_distance(self, start, end):
        self._validate_nodes_names([start, end])
        all_routes = self.discover_routes(start, end, max_nr_stops=len(self.graph.nodes))
        min_distance = sys.maxsize
        shortest_route = None

        for route in all_routes:
            route_dist = self._get_distance(route)
            if route_dist < min_distance:
                min_distance = route_dist
                shortest_route = route

        return min_distance

    def discover_routes(self, start, end, min_nr_stops=1, max_nr_stops=sys.maxsize, max_distance=sys.maxsize):
        self._validate_nodes_names([start, end])
        self._clean_is_visited()
        matched_routes = []
        current_node = self.graph.nodes[start]
        end_node = self.graph.nodes[end]

        self._discover_routes(current_node, end_node, min_nr_stops, max_nr_stops, max_distance, [current_node], matched_routes)
        return matched_routes

    def _discover_routes(self, current_node, end_node, min_nr_stops, max_nr_stops, max_distance,
                         current_route, matched_routes):
        if current_node.is_dead_end():
            return

        if current_node == end_node:
            if min_nr_stops <= len(current_route) - 1<= max_nr_stops:
                if self._get_distance(current_route) <= max_distance:
                    self._print_route(current_route)
                    matched_routes.append(list(current_route))

        if len(current_route) - 1> max_nr_stops:
            return

        if self._get_distance(current_route) > max_distance:
            return

        current_node.is_visited = True
        for key, edge in current_node.edges.items():
            next_node = edge.destination

            route = list(current_route)
            route.append(next_node)
            self._discover_routes(next_node, end_node, min_nr_stops, max_nr_stops, max_distance, route,
                                  matched_routes)

    def _print_routes(self, routes_list):
        [self._print_route(route) for route in routes_list]

    def _print_route(self, route):
        str = ''
        [str.join(node.name + '-') for node in route]
        print str
