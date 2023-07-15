"""
Muhammad Irfan Abidin / L200210021
"""
class Simpul(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    if root:
        inorder(root.left)
        print(str(root.data) + "->", end='')
        inorder(root.right)

def preorder(root):
    if root:
        print(str(root.data) + "->", end='')
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.data) + "->", end='')


a = Simpul("1")
b = Simpul("2")
c = Simpul("3")
d = Simpul("4")
e = Simpul("5")
f = Simpul("6")
g = Simpul("7")

a.left = b; a.right = c
b.left = d; b.right = e
c.left = f; c.right = g

print("Inorder traversal of the BST:")
inorder(a)
print()
print("\nPreorder traversal of the BST:")
preorder(a)
print()
print("\nPostorder traversal of the BST:")
postorder(a)

array = [4, 8, 12, 16, 20, 22, 28, 32, 35]

# Memasukkan elemen array ke dalam BST
for elemen in array:
    node = Simpul(str(elemen))
    current = a
    while True:
        if elemen < int(current.data):
            if current.left is None:
                current.left = node
                break
            else:
                current = current.left
        else:
            if current.right is None:
                current.right = node
                break
            else:
                current = current.right

print("\nInorder traversal of the BST with added array elements:")
inorder(a)
print()
print("\nPreorder traversal of the BST with added array elements:")
preorder(a)
print()
print("\nPostorder traversal of the BST with added array elements:")
postorder(a)
