class Tree:

    def __init__(self, value, parent=None, children=None):
        self.value = value
        self.parent = parent
        self.children = []

    def add_child(self, node):
        node.parent = self
        self.children.append(node)

    def __str__(self):
        return str(self.value)

