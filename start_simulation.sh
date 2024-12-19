#!/bin/bash

if [ -z "$1" ];
then
  echo "Usage: $0 <number_of_nodes>"
  exit 1
fi

NUM_NODES=$1

echo "Generating graph with $NUM_NODES nodes..."
python3 generate_graph.py $NUM_NODES

echo "Creating docker-compose.yml..."
echo "version: '3.9'" > docker-compose.yml
echo "services:" >> docker-compose.yml
for (( i=0 ; i<NUM_NODES ; i++ ));
do
  echo "  node_$i:" >> docker-compose.yml
  echo "    build: ." >> docker-compose.yml
  echo "    environment:" >> docker-compose.yml
  echo "      - NODE_ID=$i" >> docker-compose.yml
  echo "    container_name: distributed-bellman-ford_node_$i" >> docker-compose.yml
done

echo "Starting the simulation with Docker Compose..."
docker-compose up --build

echo "Collecting logs from each node..."
mkdir -p ./logs
for ((i=0 ; i<NUM_NODES ; i++ ));
do
  echo "Fetching log for node $i..."
  docker cp "distributed-bellman-ford_node_$i:/app/logs/log_node_$i.txt" "./logs/log_node_$i.txt"
done

echo "Cleaning up the Docker containers..."
docker-compose down
echo "Simulation complete. Logs saved to log_node_<node_id>.txt files."
echo "Graph image saved as 'graph_image.png'."
