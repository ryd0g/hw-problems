# Given a singly-linked list and an integer k, find the value in the kth-to-last node.

class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None
     
class LinkedList:
    def __init__(self):
        self.head = None
 
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
 
    def printkthFromLast(self, k):
        temp = self.head 
         
        length = 0
        while temp is not None:
            temp = temp.next
            length += 1
    
        if k > length: 
            print('Location is greater than the' +
                         ' length of LinkedList')
            return
        temp = self.head
        for i in range(0, length - k):
            temp = temp.next
        print(temp.data)
 
# Driver Code       
llist = LinkedList()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)
llist.printkthFromLast(2)