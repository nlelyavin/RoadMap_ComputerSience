from node import Node


class InOrder:

    def traversal_bst(self, node: Node | None):
        """Обход BST дерева In-order"""

        if node:
            self.traversal_bst(node=node.left)
            print(node.value)
            self.traversal_bst(node=node.right)
