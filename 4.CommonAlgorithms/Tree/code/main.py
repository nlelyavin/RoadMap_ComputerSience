from in_order import InOrder
from pre_order import PreOrder
from post_order import PostOrder
from node import Node


root = Node(5)
root.left = Node(3)
root.right = Node(7)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.left = Node(6)

print('--------------------------------------InOrder---------------------------------------')
in_order = InOrder()
in_order.traversal_bst(root)

print('--------------------------------------PreOrder--------------------------------------')
pre_order = PreOrder()
pre_order.traversal_bst(root)

print('--------------------------------------PostOrder--------------------------------------')
post_order = PostOrder()
post_order.traversal_bst(root)
