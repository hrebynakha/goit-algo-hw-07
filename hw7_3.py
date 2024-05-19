"""
Напишіть алгоритм (функцію), який знаходить суму всіх значень у двійковому дереві пошуку або в AVL-дереві.
Візьміть будь-яку реалізацію дерева з конспекту чи з іншого джерела

"""

import copy
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from main import root, positions, G

workflow = []
fig, ax = plt.subplots(figsize=(20, 15))

def get_sum(node, total=0):
    """Get sum of tree"""
    total += node.val
    workflow.append(node.val)
    if node.left:
        get_sum(node.left, total=total)

    if node.right:
        get_sum(node.right, total=total)

    return total
def update(frame,):
    """ Update frame"""
    ax.clear()  # Clear the previous frame
    # Nodes and labels
    nx.draw_networkx_nodes(G, pos=positions, ax=ax, node_size=300)
    nx.draw_networkx_labels(G, pos=positions, ax=ax)
    nx.draw_networkx_edges(G, pos=positions, ax=ax, edge_color='gray', alpha=0.7)
    node = workflow[frame]
    total_now = sum(workflow[0:frame])
    ax.set_title(f"Append value....{node}. Total sum now: {total_now}")  # Set the title
    nx.draw_networkx_nodes(
        G, pos=positions,nodelist=[node], ax=ax, node_size=500, node_color='red'
    )


if __name__ == "__main__":
    tree = copy.copy(root)
    total_sum = get_sum(tree)
    
    ani = FuncAnimation(fig, update, frames=len(workflow), interval=1000)
    plt.title(f"Total: {total_sum} ")
    plt.show()
