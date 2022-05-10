# Given a binary search tree, convert it into a sorted doubly-linked 
# list by modifying the original tree nodes (do not create new nodes).

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
 
class BtoDll:
    def __init__(self):
        self.head = None
        self.tail = None
 
    def convert(self, root):
       
        if root is None:
            return
           
        self.convert(root.left)
         
        node = root
        if self.head is None:
            self.head = node
        else:
            self.tail.right = node
            node.left = self.tail
        self.tail = node
         
        self.convert(root.right)
        return self.head
 
def BinaryTree2DoubleLinkedList(root):
    converter = BtoDll()
    return converter.convert(root)
 
 
def print_dll(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.right