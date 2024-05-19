"""Main file with draw and build tree function"""
import copy
import networkx as nx

G = nx.Graph()
positions = {}

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)

def add_node(node_name, **options):
    G.add_node(node_name, **options)

def add_edges(lst, **options):
    G.add_edges_from(lst, **options)

def add_pos(val, pos_x, pos_y, node_type="right"):
    append = -0.5 if node_type == "right" else 0.5
    for _, pos in positions.items():
        x, _ = pos
        if x == pos_x:
            pos_x += append
    positions[val] = (pos_x, pos_y)

def build_tree(tree, pos_x, pos_y,  node_type="right", prev=None):
    add_node(tree.val)
    add_pos(tree.val, pos_x, pos_y, node_type)
    if prev:
        add_edges([(prev,  tree.val)])

    if tree.left:
        new_x, new_y = pos_x-1.5 , pos_y-2
        build_tree(tree.left,  new_x, new_y, node_type="left", prev=tree.val)

    if tree.right:
        new_x, new_y = pos_x+1.5 , pos_y-2
        build_tree(tree.right, new_x, new_y, prev=tree.val)

root = Node(5)
root = insert(root, 3)
root = insert(root, 4)
root = insert(root, 1)
root = insert(root, 2)
root = insert(root, 10)
root = insert(root, 11)
root = insert(root, -11)
root = insert(root, -6)
root = insert(root, -9)
root = insert(root, 8)
root = insert(root, 9)
tree = copy.copy(root)
build_tree(tree, 0, 0)
