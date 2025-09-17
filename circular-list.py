#this file is to practice the implementation and functions of a circular linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def insert_node(head, key, new_data):
    
    if head == None:
        curr = Node(new_data)
        curr.next = curr
        curr.prev = curr
        return curr
    
    curr = head
    while True:
        if curr.data == key:
            new_node = Node(new_data)
            new_node.next = curr.next
            new_node.prev = curr
            curr.next.prev = new_node
            curr.next = new_node
            return head
        curr = curr.next
        if curr == head:
            break
    return head
    



def insert_at_front(head, data):
    if head == None:
        return head
    
    new = Node(data)
    new.prev = head.prev
    new.next = head
    head.prev.next = new
    tail = new.prev
    head = new
    return new


