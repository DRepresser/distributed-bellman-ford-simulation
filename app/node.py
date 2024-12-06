import json
import os

def read_graph():
    """Read the graph data from a JSON file."""
    with open("graph.json", "r") as f:
        return json.load(f)

def log_update(log_file, iteration, node, neighbor, old_distance, new_distance):
    """Log the distance update details."""
    log_file.write(
        f"Iteration {iteration}: Node {node} updated distance of Node {neighbor} "
        f"from {old_distance} to {new_distance}\n"
    )

def bellman_ford(node_id, graph):
    """
    Perform the Bellman-Ford algorithm for a specific node.
    
    Args:
        node_id (str): The ID of the current node.
        graph (dict): The adjacency list representation of the graph.

    Returns:
        dict: The final distance table for the node.
    """
    distances = {n: float("inf") for n in graph}
    distances[node_id] = 0

    # Ensure logs directory exists
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    
    log_file_path = os.path.join(log_dir, f"log_node_{node_id}.txt")
    with open(log_file_path, "w") as log_file:
        log_file.write(f"Starting Bellman-Ford for Node {node_id}\n")
        log_file.write(f"Initial distances: {json.dumps(distances)}\n\n")
        
        for iteration in range(len(graph) - 1):
            log_file.write(f"--- Iteration {iteration + 1} ---\n")
            for u in graph:
                for edge in graph[u]:
                    v, weight = edge["neighbor"], edge["weight"]
                    if distances[u] + weight < distances[v]:
                        old_distance = distances[v]
                        distances[v] = distances[u] + weight
                        log_update(log_file, iteration + 1, u, v, old_distance, distances[v])
            log_file.write(f"Distances after iteration {iteration + 1}: {json.dumps(distances)}\n\n")

    return distances

if __name__ == "__main__":
    node_id = os.environ["NODE_ID"]
    graph = read_graph()
    distances = bellman_ford(node_id, graph)
    print(f"Node {node_id} finished with distances: {distances}")
