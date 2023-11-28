class BFSNode:
    def __init__(self, value: int):
        self.value = value
        self.children = None


class BFSOrder:
    def __init__(self):
        self.queue = []

    def traversal_tree(self, root: BFSNode):
        self.queue.append(root)

