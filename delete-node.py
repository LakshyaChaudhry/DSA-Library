#delete node from singly linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_node(head, key):
    if head == None:
        return head
    
    if head == key:
        temp = head
        head = head.next
        temp = None
        return head

    prev = head
    curr = head.next
    while curr != None and curr.data != key:
        prev = curr
        curr = curr.next
    
    if curr != None:
        prev.next = curr.next
        curr = None
    return head

