class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_at_end(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def display(self):
        if not self.head:
            print("Linked list is empty")
            return
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next

# Create linked list from input
ll = LinkedList()
size = int(input())
elements = list(map(int, input().strip().split()))
for elem in elements:
    ll.insert_at_end(elem)

# Delete node at end
ll.delete_at_end()

# Output
ll.display()