class BinaryTreeNode:

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def insert(node, new_value):

    if node is None:
        node = BinaryTreeNode(new_value)
        return node
    if new_value < node.data:
        node.left_child = insert(node.left_child, new_value)
    else:
        node.right_child = insert(node.right_child, new_value)
    return node


def inorder(node):
    if node:
        inorder_array = inorder(node.left_child)
        inorder_array += [node.data]
        inorder_array += inorder(node.right_child)
    else:
        inorder_array = []
    return inorder_array


def make_tree():
    root = insert(None, 15)
    insert(root, 10)
    insert(root, 25)
    insert(root, 6)
    insert(root, 14)
    insert(root, 20)
    insert(root, 60)
    return root


root = make_tree()
print("Inorder Traversal:")
print(inorder(root))

