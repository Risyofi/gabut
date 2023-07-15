"""
Muhammad Irfan Abidin / L200210021
"""
class Simpul(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        return Simpul(data)
    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)
    return root

def build_bst(arr, data):
    root = Simpul(data)
    for value in arr:
        root = insert(root, value)
    return root

def delete(root, data):
    if root is None:
        return root
    if data < root.data:
        root.left = delete(root.left, data)
    elif data > root.data:
        root.right = delete(root.right, data)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        temp = find_min(root.right)
        root.data = temp.data
        root.right = delete(root.right, temp.data)
    return root

def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def preorder(root):
    if root:
        print(str(root.data) + "->", end='')
        preorder(root.left)
        preorder(root.right)

array = [4, 8, 12, 15, 18, 22, 24, 30, 36]

root = build_bst(array, 18)
print("BST built with root 18:")
print(root.data)  # Output: 18

print("\nPreorder traversal of the BST:")
preorder(root) # Output: 18->4->8->12->15->22->24->30->36->
print()

root = insert(root, 4)
print("\nBST after inserting a new node with value 4:")
preorder(root) # Output: 18->4->8->12->15->22->24->30->36->
print()

root = delete(root, 36)
print("\nBST after deleting a node with value 36:")
preorder(root) # Output: 18->4->8->12->15->22->24->30->
