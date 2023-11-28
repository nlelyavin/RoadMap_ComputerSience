from node import Node


class PreOrder:

    def traversal_bst(self, node: Node | None):
        """Обход BST дерева In-order"""

        if node:
            print(node.value)
            self.traversal_bst(node=node.left)
            self.traversal_bst(node=node.right)
