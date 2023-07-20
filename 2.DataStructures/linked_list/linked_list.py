"""LinkedList на python. Лучше реализовывать с помощью ООП."""
from typing import Optional

main_node = dict(value='1')

second_node = dict(value='2')

third_node = dict(value='3')

main_node['node'] = second_node
second_node['node'] = third_node


def get_next(node_: dict) -> Optional[dict]:
    return node_.get('node')


node = main_node
while node:
    print(node.get('value'))
    node = get_next(node)
