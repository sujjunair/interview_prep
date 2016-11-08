class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = -1


class BinaryTree(object):
    def __init__(self):
        self.root = None

    def _height(self, node):
        if node is None:
            return -1
        left_height = self._height(node.left)
        right_height = self._height(node.right) 

        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1

    def add(self, elem):
        """add an element to the tree
        first create the Node object with elem
        if root doesn't exist, then initialize 
        the root with the Node
        """
        if self.root == None:
            self.root = Node(elem)
            # root has no parent
            self.root.parent = None
        else:
            self._add(elem, self.root)

    def _add(self, elem, node):
        """add elem to node
        """
        if elem <= node.value:
            if node.left is not None:
                self._add(elem, node.left)
            else:
                node.left = Node(elem)
                node.left.parent = node
                node.left.height += 1
        else:
            if node.right is not None:
                self._add(elem, node.right)
            else:
                node.right = Node(elem)
                node.right.parent = node
                node.right.height += 1

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

    def inorder(self):
        return inorder(self.root)


def inorder(node):
    if node is not None:
        print "node value is = ", node.value
        inorder(node.left)
        print "======="
        print node.value
        print "======="
        inorder(node.right)
    else:
        print "node value is None"
