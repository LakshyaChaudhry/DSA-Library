#this file is for creating a doubly linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def traverse_DLL(head, key):
    curr = head
    while curr != None:
        if curr.data == key:
            return True
        curr = curr.next
    return False

def delete_node(head, key):
    if head == None:
        return head
    
    if head.data == key:
        temp = head
        head.next.prev = None
        head = head.next
        temp = None
        return head
    
    curr = head
    while curr != None and curr.data != key:
        curr = curr.next
    
    if curr != None:
        curr.next.prev = curr.prev
        curr.prev.next = curr.next
        curr = None
    return head




