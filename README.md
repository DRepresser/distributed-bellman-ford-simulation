# distributed-bellman-ford-simulation

This project is a distributed simulation of the Bellman-Ford algorithm, designed for CSS324 Network Computing. It demonstrates how nodes in a distributed system work collaboratively to compute the shortest path in a network. The system uses Docker to simulate a distributed environment where each node is represented by a container.

## Objective

The objective of this project is to:

1. Demonstrate the concept of the Distributed Bellman-Ford algorithm.
2. Show how nodes communicate dynamically in a distributed network to compute shortest paths.
3. Provide an interactive and modular setup using Docker and Flask.

## Project Structure

```bash
distributed-bellman-ford/
├── docker-compose.yml       # Configures and orchestrates the containers for the nodes
├── node/
│   ├── Dockerfile           # Specifies the node container configuration
│   ├── app.py               # Node logic and REST API for communication
│   ├── graph.json           # Defines the network graph structure
│   └── requirements.txt     # Python dependencies
```

## How It Works

1. Graph Definition:
    - The graph is defined in graph.json, specifying each node's neighbors and edge weights.

2. Node Containers:
    - Each node in the graph runs as a separate Docker container.
    - Nodes communicate with their neighbors using a REST API implemented in Flask.

3. Algorithm Flow:
    - Each node initializes its shortest path distance to infinity, except for the source node (distance = 0).
    - Periodically, each node sends its distance updates to its neighbors.
    - Nodes update their distance values if they receive shorter paths from their neighbors.
    - The process continues until all nodes converge (no updates occur).

## Technologies Used

- Python: For implementing the algorithm and REST API.
- Flask: Lightweight framework to handle inter-node communication.
- Docker: To create isolated environments for each node.
- Docker Compose: To manage and orchestrate multiple containers.

## Setup and Execution

### Prerequisites

- Install Docker and Docker Compose on your machine.

### Steps

1. Clone the Repository:

```bash
git clone https://github.com/DRepresser/distributed-bellman-ford-simulation.git
cd distributed-bellman-ford
```

2. Build and Start the Containers:

```bash
docker-compose up --build
```

3. View Logs:
    - Observe the inter-node communication in the terminal logs.
    - Logs show distance updates and convergence of the algorithm.

4. Stop the Simulation:

```bash
docker-compose down
```

## Customizing the Graph

- Update the node/graph.json file to define your custom graph.
- Example:

```json
{
  "nodes": {
    "1": {"neighbors": {"2": 1, "3": 4}},
    "2": {"neighbors": {"3": 2, "4": 6}},
    "3": {"neighbors": {"4": 3}},
    "4": {"neighbors": {}}
  }
}
```

- Rebuild and start the containers:

```bash
docker-compose up --build
```
