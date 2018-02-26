# Train Routes Problem

This document describes the design behind my solution for the train routes problem and how-to run the application. 

## Project Structure

Though the problem is simple. OOP patters are followed with backend-style setup. Therefore you can find two seperate directories:

1- `src` with:
- **model**: The basic data structure for the problem with `graph` (a hashmap of nodes), `node` (a hashmap of edges) and `edge` (linking source node with the destination for a given weight.)
- **controllers**: with `graph_importer` (to handle file import and serving as a simple graph factory) and `graph_operations` (for the different operation we want to implement like `shortest_distance`, `discover_route`,.. etc.)
- **data**: contains the graph representation in a text file.
- **exceptions**: for our custom exceptions. Currently it only has one simple exception of `NodeNameNotExistsError`.

2- and `test`.

### Prerequisites

`python 3.+` can work.


## Running the tests
1- via command line, navigate to the directory:
```
cd train-route-problem
```

2- run all the tests (2 files with 7 tests to cover the 10 cases):
```
python -m unittest discover /Users/mohammadshaker/PycharmProjects/train-route-problem/test
```


### Break down into end to end tests

1- with `test_distances`, we test the cases 1 through 5:

```
self.assertEqual(self.graph_operations.get_distance(_split('A-B-C')), 9)
self.assertEqual(self.graph_operations.get_distance(_split('A-D')), 5)
self.assertEqual(self.graph_operations.get_distance(_split('A-D-C')), 13)
self.assertEqual(self.graph_operations.get_distance(_split('A-E-B-C-D')), 22)
self.assertEquals(self.graph_operations.get_distance(_split('A-E-D')), NO_SUCH_ROUTE)
```

2- with `test_nr_routes_with_max_stops`, we test the cases 6 and 7:

```
self.assertEqual(len(self.graph_operations.discover_routes('C', 'C', 1, 3)), 2)
self.assertEqual(len(self.graph_operations.discover_routes('A', 'C', 4, 4)), 3)
```
1- with `test_distances`, we test the cases 1 through 5:

```
self.assertEqual(self.graph_operations.shortest_routes_distance('A', 'C'), 9)
self.assertEqual(self.graph_operations.shortest_routes_distance('B', 'B'), 9)
```
1- with `test_distances`, we test the cases #10 (`max_distance=29`, since the max is included and therefore `<30`):

```
self.assertEqual(len(self.graph_operations.discover_routes('C', 'C', max_distance=29)), 7)
```

## Questions

* For any question please contact me via: `mohammadshakergtr`
