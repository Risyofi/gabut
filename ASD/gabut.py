class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    return root

def delete(root, value):
    if root is None:
        return root
    if value < root.value:
        root.left = delete(root.left, value)
    elif value > root.value:
        root.right = delete(root.right, value)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        root.value = minValue(root.right)
        root.right = delete(root.right, root.value)
    return root

def minValue(node):
    current = node
    while current.left is not None:
        current = current.left
    return current.value

def buildBST(array, root_value):
    root = Node(root_value)
    for value in array:
        insert(root, value)
    return root

def preorderTraversal(root):
    if root is not None:
        print(root.value, end=" ")
        preorderTraversal(root.left)
        preorderTraversal(root.right)

def inorderTraversal(root):
    if root is not None:
        inorderTraversal(root.left)
        print(root.value, end=" ")
        inorderTraversal(root.right)

def postorderTraversal(root):
    if root is not None:
        postorderTraversal(root.left)
        postorderTraversal(root.right)
        print(root.value, end=" ")

# Array
array = [4, 8, 12, 15, 18, 22, 24, 30, 36]

# Build BST manually with root 18
root_manual = buildBST(array, 18)

# Insert a new node with value 4
insert(root_manual, 4)

# Delete the node with value 36
delete(root_manual, 36)

# Preorder Traversal
print("Preorder Traversal:")
preorderTraversal(root_manual)
print()

# Inorder Traversal
print("Inorder Traversal:")
inorderTraversal(root_manual)
print()

# Postorder Traversal
print("Postorder Traversal:")
postorderTraversal(root_manual)
print()
