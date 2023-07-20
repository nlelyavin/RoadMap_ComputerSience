from typing import Optional, List


class Node:
    def __init__(self, value: int):
        self._value = value
        self.child_nodes = []

    def __str__(self):
        return str(self._value)

    def __repr__(self):
        return str(self._value)


class Tree:
    def __init__(self, root: Node) -> None:
        self._root = root

    def append(self, node: Node) -> None:
        self._root.child_nodes.append(node)

    def search(self, item: int) -> Optional[Node]:
        pass

    def get_elements(self, root: Node) -> List:
        """Возвращает все значения дерева. Используется рекурсия"""

        nodes = [root]

        children = root.child_nodes
        for child in children:
            descendants = self.get_elements(child)
            nodes.extend(descendants)

        return nodes

    def __str__(self):
        """Все значения дерева"""

        nodes = self.get_elements(self._root)

        return str(nodes)


tree = Tree(Node(1))
node2 = Node(2)
node3 = Node(3)
tree.append(node2)
tree.append(node3)
print(tree)
