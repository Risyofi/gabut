##    Muhammad Irfan Abidin
##    L200210021/A
print('--Muhammad Irfan Abidin/L200210021--')

class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None
    
    def insertAtEnd(self, data):
        newnode = node(data)
        if self.head is None:
            self.head = newnode
            return
        lastnode = self.head
        while lastnode.next:
            lastnode = lastnode.next
        lastnode.next = newnode

    def insertAtStart(self, data):
        newnode = node(data)
        newnode.next = self.head
        self.head = newnode

    def insertAtMiddle(self, middle_node, data):
        if not middle_node:
            return False
        newnode = node(data)
        newnode.next = middle_node.next
        middle_node.next = newnode

    def delete(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        prevnode = None
        currnode = self.head
        while currnode and currnode.data != data:
            prevnode = currnode
            currnode = currnode.next
        if currnode is None:
            return
        prevnode.next = currnode.next

    def print_list(self):
        currnode = self.head
        while currnode:
            print(currnode.data)
            currnode = currnode.next

    def hitung_nodes(self):
        count = 0
        currnode = self.head
        while currnode:
            count += 1
            currnode = currnode.next
        return count
    
    def reverse(self):
        prevnode = None
        currnode = self.head
        while currnode:
            nextnode = currnode.next
            currnode.next = prevnode
            prevnode = currnode
            currnode = nextnode
        self.head = prevnode

## Output
llist = linkedList()

print('insert at end')
llist.insertAtEnd(8)
llist.insertAtEnd(9)
llist.insertAtEnd(10)
llist.print_list()

print('insert at start')
llist.insertAtStart(3)
llist.insertAtStart(2)
llist.print_list()

print('insert at middle')
middle_node = llist.head.next
llist.insertAtMiddle(middle_node, 6)
llist.print_list()

print('delete node')
llist.delete(8)
llist.print_list()

print('hitung nodes')
print(llist.hitung_nodes())

print('reverse nodes')
llist.reverse()
llist.print_list()
