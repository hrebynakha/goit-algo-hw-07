"""
Напишіть алгоритм (функцію), який знаходить найменше значення
у двійковому дереві пошуку або в AVL-дереві.
Візьміть будь-яку реалізацію дерева з конспекту чи з іншого джерела
"""
import copy
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from main import root, positions, G

left_nodes = []
fig, ax = plt.subplots(figsize=(20, 15))

def get_min(node, ):
    """Get minimum value"""
    left_nodes.append(node.val)
    if node.left:
        get_min(node.left )
    return node.val

def update(frame,):
    """ Update frame"""
    ax.clear()  # Clear the previous frame
    # Nodes and labels
    nx.draw_networkx_nodes(G, pos=positions, ax=ax, node_size=300)
    nx.draw_networkx_labels(G, pos=positions, ax=ax)
    nx.draw_networkx_edges(G, pos=positions, ax=ax, edge_color='gray', alpha=0.7)
    node = left_nodes[frame]
    ax.set_title(f"Searching for minimum value....{node}")  # Set the title
    nx.draw_networkx_nodes(
        G, pos=positions,nodelist=[node], ax=ax, node_size=500, node_color='red'
    )

if __name__ == "__main__":
    tree = copy.copy(root)
    min_el = get_min(tree)
    ani = FuncAnimation(fig, update, frames=len(left_nodes), interval=1000)
    plt.title(f"Minimum value: {min_el} ")
    plt.show()
