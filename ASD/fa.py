import matplotlib.pyplot as plt

class Simpul:
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

def draw_tree(node, x, y, x_unit, y_unit):
    if node:
        plt.text(x, y, str(node.data), ha='center', va='center', 
                 bbox=dict(facecolor='white', edgecolor='black', boxstyle='circle'))
        if node.left:
            plt.plot([x, x - x_unit], [y, y - y_unit], 'k-')
            draw_tree(node.left, x - x_unit, y - y_unit, x_unit / 2, y_unit)
        if node.right:
            plt.plot([x, x + x_unit], [y, y - y_unit], 'k-')
            draw_tree(node.right, x + x_unit, y - y_unit, x_unit / 2, y_unit)

array = [4, 8, 12, 15, 18, 22, 24, 30, 36]
root = build_bst(array, 18)

plt.figure(figsize=(8, 8))
draw_tree(root, 0, 0, 4, 4)
plt.axis('off')
plt.show()
