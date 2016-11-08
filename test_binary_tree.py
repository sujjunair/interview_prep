from binary_tree import BinaryTree

def test_binary_tree():
    b = BinaryTree()
    b.add(4)
    b.add(2)
    b.add(5)
    b.add(3)
    b.add(1)
    b.inorder()


def main():
    test_binary_tree()

if __name__=="__main__":
    main()
