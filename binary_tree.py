class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self):
        self.root = None
       
    def add(self, elem):
        if self.root == None:
            self.root = Node(elem)
        else:
            self._add(elem, self.root)

    def _add(self, elem, node):
        if elem <= node.value:
            if node.left is not None:
                self._add(elem, node.left)
            else:
                node.left = Node(elem)
        else:
            if node.right is not None:
                self._add(elem, node.right)
            else:
                node.right = Node(elem)

    def find(self, value):
        if self.root is not None:
            self._find(value, self.root)

    def _find(self, value, node):
        if value == node.value:
            return node
        elif value < node.value: 
            if node.left is not None:
                self._find(value, node.left)
            else:
                return None # element doesn't exist in tree
        elif value > node.value:
            if node.right is not None:
                self._find(value, node.right)
            else:
                return None

