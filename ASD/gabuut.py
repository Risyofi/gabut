from collections import deque
import matplotlib.pyplot as plt
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_perfect_binary_tree(root):
    def calculate_height(node):
        if node is None:
            return 0
        return 1 + max(calculate_height(node.left), calculate_height(node.right))

    def check_perfect_binary_tree(node, height, level):
        if node is None:
            return True

        if node.left is None and node.right is None:
            return height == level + 1

        if node.left is None or node.right is None:
            return False

        return check_perfect_binary_tree(node.left, height, level + 1) and check_perfect_binary_tree(node.right, height, level + 1)

    height = calculate_height(root)
    return check_perfect_binary_tree(root, height, 0)

def is_full_binary_tree(root):
    if root is None:
        return True

    if root.left is None and root.right is None:
        return True

    if root.left is not None and root.right is not None:
        return is_full_binary_tree(root.left) and is_full_binary_tree(root.right)

    return False

def is_complete_binary_tree(root):
    if root is None:
        return True

    queue = deque()
    queue.append(root)
    has_missing = False

    while queue:
        node = queue.popleft()

        if node is None:
            has_missing = True
        elif has_missing:
            return False
        else:
            queue.append(node.left)
            queue.append(node.right)

    return True

def calculate_tree_size(root):
    if root is None:
        return 0

    return 1 + calculate_tree_size(root.left) + calculate_tree_size(root.right)

def calculate_tree_height(root):
    if root is None:
        return -1

    return 1 + max(calculate_tree_height(root.left), calculate_tree_height(root.right))

def calculate_tree_width(root):
    if root is None:
        return 0

    queue = deque()
    queue.append(root)
    max_width = 0

    while queue:
        level_width = len(queue)
        max_width = max(max_width, level_width)

        for _ in range(level_width):
            node = queue.popleft()

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return max_width
"""
def plot_binary_tree(root, x, y, x_shift, y_shift):
    if root is None:
        return

    plt.text(x, y, str(root.value), color='black', weight='bold', ha='center', va='center',
             bbox=dict(facecolor='white', edgecolor='black', boxstyle='circle'))

    if root.left is not None:
        plt.plot([x, x - x_shift], [y, y - y_shift], color='black')
        plot_binary_tree(root.left, x - x_shift, y - y_shift, x_shift / 2, y_shift)

    if root.right is not None:
        plt.plot([x, x + x_shift], [y, y - y_shift], color='black')
        plot_binary_tree(root.right, x + x_shift, y - y_shift, x_shift / 2, y_shift)
"""
def plot_binary_tree(node, ax, x, y, dx, dy):
    if node is None:
        return

    ax.text(x, y, str(node.data), color='black', weight='bold', ha='center', va='center',
             bbox=dict(facecolor='white', edgecolor='black', boxstyle='circle'))

    if node.left is not None:
        ax.plot([x, x - dx], [y, y - dy], color='black')
        plot_binary_tree(node.left, ax, x - dx, y - dy, dx/2, dy/2)

    if node.right is not None:
        ax.plot([x, x + dx], [y, y - dy], color='black')
        plot_binary_tree(node.right, ax, x + dx, y - dy, dx/2, dy/2)


def visualize_binary_tree(root):
    fig, ax = plt.subplots(figsize=(8, 8))
    plt.axis('off')
    plot_binary_tree(root, 0, 0, 50, 50)
    plt.show()
    
def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.value:
        root.left = insert(root.left, data)
    elif data > root.value:
        root.right = insert(root.right, data)
    return root

def build_bst(arr, data):
    root = Node(data)
    for value in arr:
        root = insert(root, value)
    return root

array = [4, 8, 12, 15, 18, 22, 24, 30, 36]
root = build_bst(array, 18)

visualize_binary_tree(root)

"""
a = Node("1")
b = Node("2")
c = Node("3")
d = Node("4")
e = Node("5")
f = Node("6")
g = Node("7")

a.left = b; a.right = c
b.left = d; b.right = e
c.left = f; c.right = g
visualize_binary_tree(a)
# Contoh pohon biner
#        1
#       / \
#      2   3
#     / \   \
#    4   5   6
#         \
#          7
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
root.left.right.right = Node(7)

width = calculate_tree_width(root)
print("Lebar pohon biner:", width)

size = calculate_tree_size(root)
height = calculate_tree_height(root)

print("Ukuran pohon biner:", size)
print("Ketinggian pohon biner:", height)

if is_perfect_binary_tree(root):
    print("Pohon biner adalah pohon biner sempurna.")
else:
    print("Pohon biner bukan pohon biner sempurna.")

if is_full_binary_tree(root):
    print("Pohon biner adalah pohon biner penuh.")
else:
    print("Pohon biner bukan pohon biner penuh.")

if is_complete_binary_tree(root):
    print("Pohon biner adalah pohon biner komplet.")
else:
    print("Pohon biner bukan pohon biner komplet.")



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(6)
root.left.right.right = Node(7)

width = calculate_tree_width(root)
print("Lebar pohon biner:", width)

size = calculate_tree_size(root)
height = calculate_tree_height(root)

print("Ukuran pohon biner:", size)
print("Ketinggian pohon biner:", height)

if is_perfect_binary_tree(root):
    print("Pohon biner adalah pohon biner sempurna.")
else:
    print("Pohon biner bukan pohon biner sempurna.")

if is_full_binary_tree(root):
    print("Pohon biner adalah pohon biner penuh.")
else:
    print("Pohon biner bukan pohon biner penuh.")

if is_complete_binary_tree(root):
    print("Pohon biner adalah pohon biner komplet.")
else:
    print("Pohon biner bukan pohon biner komplet.")

print()


### b
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.left.right.left = Node(10)
root.left.right.right = Node(11)
root.right.left.left = Node(12)
root.right.left.right = Node(13)
root.right.right.left = Node(14)
root.right.right.right = Node(15)

width = calculate_tree_width(root)
print("Lebar pohon biner:", width)

size = calculate_tree_size(root)
height = calculate_tree_height(root)

print("Ukuran pohon biner:", size)
print("Ketinggian pohon biner:", height)

if is_perfect_binary_tree(root):
    print("Pohon biner adalah pohon biner sempurna.")
else:
    print("Pohon biner bukan pohon biner sempurna.")

if is_full_binary_tree(root):
    print("Pohon biner adalah pohon biner penuh.")
else:
    print("Pohon biner bukan pohon biner penuh.")

if is_complete_binary_tree(root):
    print("Pohon biner adalah pohon biner komplet.")
else:
    print("Pohon biner bukan pohon biner komplet.")


print()


### c
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(6)
root.left.right.right = Node(7)
root.left.right.left.right = Node(8)
root.left.right.left.right.left = Node(9)
root.left.right.left.right.right = Node(10)
root.left.right.left.right.left.left = Node(11)
root.left.right.left.right.left.right = Node(12)
root.left.right.left.right.left.right.left = Node(13)
root.left.right.left.right.left.right.right = Node(14)

width = calculate_tree_width(root)
print("Lebar pohon biner:", width)

size = calculate_tree_size(root)
height = calculate_tree_height(root)

print("Ukuran pohon biner:", size)
print("Ketinggian pohon biner:", height)

if is_perfect_binary_tree(root):
    print("Pohon biner adalah pohon biner sempurna.")
else:
    print("Pohon biner bukan pohon biner sempurna.")

if is_full_binary_tree(root):
    print("Pohon biner adalah pohon biner penuh.")
else:
    print("Pohon biner bukan pohon biner penuh.")

if is_complete_binary_tree(root):
    print("Pohon biner adalah pohon biner komplet.")
else:
    print("Pohon biner bukan pohon biner komplet.")


print()


root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.left.left.left = Node(5)
root.left.right.left = Node(6)
root.left.right.right = Node(7)

width = calculate_tree_width(root)
print("Lebar pohon biner:", width)

size = calculate_tree_size(root)
height = calculate_tree_height(root)

print("Ukuran pohon biner:", size)
print("Ketinggian pohon biner:", height)

if is_perfect_binary_tree(root):
    print("Pohon biner adalah pohon biner sempurna.")
else:
    print("Pohon biner bukan pohon biner sempurna.")

if is_full_binary_tree(root):
    print("Pohon biner adalah pohon biner penuh.")
else:
    print("Pohon biner bukan pohon biner penuh.")

if is_complete_binary_tree(root):
    print("Pohon biner adalah pohon biner komplet.")
else:
    print("Pohon biner bukan pohon biner komplet.")


print()


### e
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.left.right.left = Node(7)
root.left.right.right = Node(8)
root.right.left.left = Node(9)
root.right.right.left = Node(10)
root.right.right.right = Node(11)
width = calculate_tree_width(root)
print("Lebar pohon biner:", width)

size = calculate_tree_size(root)
height = calculate_tree_height(root)

print("Ukuran pohon biner:", size)
print("Ketinggian pohon biner:", height)

if is_perfect_binary_tree(root):
    print("Pohon biner adalah pohon biner sempurna.")
else:
    print("Pohon biner bukan pohon biner sempurna.")

if is_full_binary_tree(root):
    print("Pohon biner adalah pohon biner penuh.")
else:
    print("Pohon biner bukan pohon biner penuh.")

if is_complete_binary_tree(root):
    print("Pohon biner adalah pohon biner komplet.")
else:
    print("Pohon biner bukan pohon biner komplet.")


print()
"""