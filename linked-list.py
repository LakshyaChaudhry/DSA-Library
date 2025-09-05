class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def insert_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

def ll_search(head, target):
    current = head
    while current:
        if current.data == target:
            return True
        current = current.next
    return False

