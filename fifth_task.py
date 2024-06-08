from fourth_task import Node


import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


def dfs(node, visit_order, graph, colors, layer=0):
    if node is not None:
        # Задаємо колір для вузла, який стає світлішим з кожним кроком
        color = (
            f"#{hex(255 - layer * 8)[2:].zfill(2)}{hex(128 + layer * 8)[2:].zfill(2)}FF"
        )
        node.color = color
        visit_order.append(node)
        colors[node.id] = node.color
        graph.add_node(node.id, color=node.color, label=node.val)

        if node.left:
            graph.add_edge(node.id, node.left.id)
            dfs(node.left, visit_order, graph, colors, layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            dfs(node.right, visit_order, graph, colors, layer + 1)


def bfs(root):
    queue = deque([root])
    visit_order = []
    colors = {}
    layer = 0
    while queue:
        node = queue.popleft()
        color = (
            f"#{hex(255 - layer * 8)[2:].zfill(2)}FF{hex(128 + layer * 8)[2:].zfill(2)}"
        )
        node.color = color
        visit_order.append(node)
        colors[node.id] = node.color
        layer += 1
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return visit_order, colors


def draw_tree(visit_order, tree, pos, colors):
    labels = {node.id: node.val for node in visit_order}
    node_colors = [colors[node.id] for node in visit_order]

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree,
        pos=pos,
        labels=labels,
        node_color=node_colors,
        with_labels=True,
        node_size=2000,
        font_size=16,
    )
    plt.show()


# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# DFS
tree = nx.DiGraph()
pos = {}
colors = {}
visit_order = []
dfs(root, visit_order, tree, colors)
pos = nx.spring_layout(tree)
draw_tree(visit_order, tree, pos, colors)

# BFS
visit_order, colors = bfs(root)
tree = nx.DiGraph()
for node in visit_order:
    tree.add_node(node.id, color=node.color, label=node.val)
    if node.left:
        tree.add_edge(node.id, node.left.id)
    if node.right:
        tree.add_edge(node.id, node.right.id)
pos = nx.spring_layout(tree)
draw_tree(visit_order, tree, pos, colors)
