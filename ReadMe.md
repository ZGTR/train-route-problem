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

2- run all the tests (2 files) with:
```
python -m unittest discover /Users/mohammadshaker/PycharmProjects/train-route-problem/test
```



### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc
