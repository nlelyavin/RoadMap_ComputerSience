from node import Node


class PostOrder:

    def traversal_bst(self, node: Node | None):
        """Обход BST дерева In-order"""

        if node:
            self.traversal_bst(node=node.left)
            self.traversal_bst(node=node.right)
            print(node.value)
