import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
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


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def array_to_heap_tree(arr, index=0):
    """
    Рекурсивно будує бінарне дерево з масиву.
    :param arr: Масив елементів бінарної купи
    :param index: Поточний індекс елементу в масиві
    :return: Кореневий вузол бінарної купи
    """
    if index >= len(arr):
        return None

    node = Node(arr[index])

    left_index = 2 * index + 1
    right_index = 2 * index + 2

    node.left = array_to_heap_tree(arr, left_index)
    node.right = array_to_heap_tree(arr, right_index)

    return node


# Приклад використання
if __name__ == "__main__":
    heap_array = [50, 30, 20, 15, 10, 8, 16]
    root = array_to_heap_tree(heap_array)
    draw_tree(root)
