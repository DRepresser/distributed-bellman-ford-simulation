from flask import Flask, request, jsonify
import threading
import requests
import os
import time

app = Flask(__name__)

# Load graph structure
with open("graph.json", "r") as f:
    graph = eval(f.read())

# Environment variable to identify the node
NODE_ID = os.getenv("NODE_ID", "1")
PORT = 5000 + int(NODE_ID)

# Node-specific details
neighbors = graph["nodes"][NODE_ID]["neighbors"]
distances = {NODE_ID: 0}  # Distance to self is 0; others initialized later
for neighbor in neighbors.keys():
    distances[neighbor] = float("inf")

# Lock for thread-safe updates
lock = threading.Lock()

# Global variable to check for convergence
updated = False


def send_updates():
    """Send current distances to neighbors periodically."""
    global updated
    while True:
        time.sleep(2)  # Simulate periodic update
        with lock:
            for neighbor, weight in neighbors.items():
                url = f"http://node{neighbor}:5000/update"
                data = {"source": NODE_ID, "distance": distances[NODE_ID] + weight}
                try:
                    requests.post(url, json=data)
                except Exception as e:
                    print(f"Error sending to node {neighbor}: {e}")
            updated = False


@app.route("/update", methods=["POST"])
def update_distance():
    """Handle distance updates from neighbors."""
    global updated
    data = request.get_json()
    source = data["source"]
    new_distance = data["distance"]
    with lock:
        if new_distance < distances[source]:
            distances[source] = new_distance
            updated = True
    return jsonify({"status": "updated"})


@app.route("/distances", methods=["GET"])
def get_distances():
    """Get current distances."""
    with lock:
        return jsonify(distances)


if __name__ == "__main__":
    # Start update thread
    threading.Thread(target=send_updates, daemon=True).start()

    # Run Flask app
    app.run(host="0.0.0.0", port=PORT)
