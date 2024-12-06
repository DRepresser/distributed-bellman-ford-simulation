import random
import networkx as nx
import matplotlib.pyplot as plt
import json
import sys

def generate_graph(num_nodes, edge_removal_prob=0.3):
    G = nx.erdos_renyi_graph(num_nodes, 0.8)

    edges_to_remove = []
    for u, v in G.edges():
        if random.random() < edge_removal_prob:
            edges_to_remove.append((u, v))

    G.remove_edges_from(edges_to_remove)

    graph_dict = {}
    for node in G.nodes():
        graph_dict[node] = []
    for u, v in G.edges():
        weight = random.randint(1, 10)
        graph_dict[u].append({"neighbor": f"{v}", "weight": weight})
        graph_dict[v].append({"neighbor": f"{u}", "weight": weight})

    with open("app/graph.json", "w") as f:
        json.dump(graph_dict, f, indent=4)

    plt.figure(figsize=(8, 8))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=12, font_weight='bold', edge_color='gray')
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title("Generated Graph")
    plt.savefig("app/graph_image.png")

    print(f"Graph generated with {num_nodes} nodes and saved as 'graph_image.png'.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 generate_graph.py <number_of_nodes>")
        sys.exit(1)

    num_nodes = int(sys.argv[1])
    generate_graph(num_nodes)
