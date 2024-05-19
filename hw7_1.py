"""
Напишіть алгоритм (функцію), який знаходить найбільше значення
у двійковому дереві пошуку або в AVL-дереві. 
Візьміть будь-яку реалізацію дерева з конспекту чи з іншого джерела.
"""
import copy
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from main import root, positions, G

right_nodes = []
fig, ax = plt.subplots(figsize=(20, 15))

def get_max(node, ):
    """Get maximum value in tree"""
    right_nodes.append(node.val)
    if node.right:
        get_max(node.right)
    return node.val

def update(frame,):
    """ Update frame"""
    ax.clear()  # Clear the previous frame
    # Nodes and labels
    nx.draw_networkx_nodes(G, pos=positions, ax=ax, node_size=300)
    nx.draw_networkx_labels(G, pos=positions, ax=ax)
    nx.draw_networkx_edges(G, pos=positions, ax=ax, edge_color='gray', alpha=0.7)
    node = right_nodes[frame]
    ax.set_title(f"Searching for maximum value....{node}")  # Set the title
    nx.draw_networkx_nodes(
        G, pos=positions,nodelist=[node], ax=ax, node_size=500, node_color='red'
    )

if __name__ == "__main__":
    tree = copy.copy(root)
    max_el = get_max(tree)
    ani = FuncAnimation(fig, update, frames=len(right_nodes), interval=1000)
    plt.title(f"Maximum value: {max_el} ")
    plt.show()
