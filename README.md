# distributed-bellman-ford-simulation

This project demonstrates the Distributed Bellman-Ford Algorithm in a simulated distributed network environment using Docker. Each node in the network runs as a separate Docker container, communicating with its neighbors to collaboratively compute the shortest paths in the graph.

This project was created for CSS324: Network Computing.

## Features

- Simulates a distributed system with multiple nodes (containers).
- Implements the Bellman-Ford algorithm for finding shortest paths in a network.
- Uses Flask for inter-node communication via REST APIs.
- Modular design for customizing the graph structure.
- Visualizes the process of convergence through logs and API responses.

## Project Structure

```bash
distributed-bellman-ford/
├── docker-compose.yml       # Configures and orchestrates containers
├── node/
│   ├── Dockerfile           # Docker configuration for each node
│   ├── app.py               # Node logic and REST API
│   ├── graph.json           # Graph structure with neighbors and weights
│   └── requirements.txt     # Python dependencies
```

## Technologies Used

- Python: For implementing the algorithm and REST API.
- Flask: Lightweight framework to handle inter-node communication.
- Docker: To create isolated environments for each node.
- Docker Compose: To manage and orchestrate multiple containers.

## How It Works

1. Graph Setup:
    - The graph is defined in graph.json, specifying each node's neighbors and edge weights.

2. Node Behavior:
    - Each node runs as a Docker container.
    - Nodes send their current shortest distance estimates to neighbors periodically.
    - If a shorter path is found, the node updates its distance and informs its neighbors.

3. Algorithm Execution:
    - Each node initializes its shortest path distance to infinity, except for the source node (distance = 0).
    - Periodically, each node sends its distance updates to its neighbors.
    - Nodes update their distance values if they receive shorter paths from their neighbors.
    - The process continues until all nodes converge (no updates occur).

## Setup and Execution

### Prerequisites

- Docker and Docker Compose installed on your system.

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

3. Access the node APIs:
    - Check the distances at any node using:
      ```bash
      http://localhost:5001/distances
      http://localhost:5002/distances
      ```
    - Replace 5001 with the appropriate port for other nodes (5002, 5003, etc.).

4. Stop the containers:

    ```bash
    docker-compose down
    ```

## Customizing the Graph

1. Open node/graph.json and define your graph.

    Example:

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

- Rebuild and restart the containers:

  ```bash
  docker-compose up --build
  ```

## Endpoints

- GET /distances:
  
  Returns the current shortest distances from the node to all other nodes.

  ```bash
  curl http://localhost:5001/distances
  ```

  Example Response:

  ```json
  {
    "1": 0,
    "2": 1,
    "3": 3,
    "4": 6
  }
  ```

- POST /update:

  Internal endpoint for nodes to receive distance updates from neighbors.
