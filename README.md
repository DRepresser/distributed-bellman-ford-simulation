# Distributed Bellman-Ford Simulation

This project was created for **CSS324: Network Computing**. It simulates the Distributed Bellman-Ford algorithm using Docker to manage multiple nodes and process the graph.

## Overview

The Distributed Bellman-Ford algorithm is used to find the shortest paths from a source node to all other nodes in a graph, even when edge weights are negative. This simulation uses Docker containers to emulate multiple nodes in the graph, and logs the algorithm's process of updating distances.

## Features

- **Docker-based simulation**: Each node runs in a separate Docker container.
- **Dynamic graph generation**: Random graphs are generated with configurable numbers of nodes and edges.
- **Log collection**: Logs are saved during the simulation to track the distance updates for each node.
- **Graph Visualization**: Generates and saves a visual representation of the graph.

## Requirements

To run the simulation, you need the following installed:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/)
- Python 3.x with the following libraries:
  - `networkx`
  - `matplotlib`

### Installing Python dependencies:

```bash
pip install networkx matplotlib
```

## Usage

### 1. Run the simulation

To start the simulation, execute the following command:

```bash
bash start_simulation.sh <NUM_NODES>
```

Replace <NUM_NODES> with the number of nodes you want to simulate.

### 2. Check logs

Logs from the simulation will be saved in the `logs/` directory. You can check the log files for detailed updates on the distance updates for each node.

### 3. Visualize the graph

A graphical representation of the generated graph will be saved as `graph.png` in the `app/` directory.
