import uuid
import networkx as nx
import matplotlib.pyplot as plt
import colorsys
from collections import deque


class Node:
    def __init__(self, key, color="#000000"):
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
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, highlight=None):
    plt.ion()
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.clf()
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors, font_size=10, font_color="white")
    plt.pause(1)


def get_color(percentage, color_type):
    if color_type == "dfs":
        h = 0.15
    elif color_type == "bfs":
        h = 0.33
    s = 0.9
    v = 0.3 + 0.7 * percentage
    rgb = colorsys.hsv_to_rgb(h, s, v)
    return '#{:02x}{:02x}{:02x}'.format(int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))


def reset_colors(node):
    if node:
        node.color = "#000000"
        reset_colors(node.left)
        reset_colors(node.right)


def dfs_visualization(root):
    if not root:
        return

    stack = [root]
    visited = []
    step = 0

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            step += 1
            node.color = get_color(step / 10, "dfs")
            draw_tree(root)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    reset_colors(root)
    draw_tree(root)


def bfs_visualization(root):
    if not root:
        return

    queue = deque([root])
    visited = []
    step = 0

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            step += 1
            node.color = get_color(step / 10, "bfs")
            draw_tree(root)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    reset_colors(root)
    draw_tree(root)


def array_to_heap_tree(arr, index=0):
    if index >= len(arr):
        return None

    node = Node(arr[index])

    left_index = 2 * index + 1
    right_index = 2 * index + 2

    node.left = array_to_heap_tree(arr, left_index)
    node.right = array_to_heap_tree(arr, right_index)

    return node


if __name__ == "__main__":
    heap_array = [50, 30, 20, 15, 10, 8, 16]
    root = array_to_heap_tree(heap_array)

    print("DFS Візуалізація:")
    dfs_visualization(root)

    print("BFS Візуалізація:")
    bfs_visualization(root)
