import uuid

import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue") -> None:
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )
    plt.show()


def add_edges_heap(graph, node, pos, index=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        left_index = 2 * index
        right_index = left_index + 1
        pos[node.id] = (index, 0)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            pos[node.left.id] = (left_index, -1)
            add_edges_heap(graph, node.left, pos, left_index)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            pos[node.right.id] = (right_index, -1)
            add_edges_heap(graph, node.right, pos, right_index)
    return graph


def draw_heap(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (1, 0)}
    tree = add_edges_heap(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(12, 8))
    nx.draw(
        tree,
        pos=pos,
        labels=labels,
        arrows=False,
        node_size=3000,
        node_color=colors,
        with_labels=True,
    )
    plt.show()


root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)
draw_heap(root)
