# Given an array of k singly-linked lists, each of whose values are in sorted order, combine all nodes (do not create new nodes) into one singly-linked list with all values in order.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
class LinkedList:
    def __init__(self):
        self.head = None
 
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    def addToList(self, newData):
        newNode = Node(newData)
        if self.head is None:
            self.head = newNode
            return
 
        last = self.head
        while last.next:
            last = last.next
 
        last.next = newNode
 
def mergeLists(headA, headB):
 
    dummyNode = Node(0)
 
    tail = dummyNode
    while True:
 
        if headA is None:
            tail.next = headB
            break
        if headB is None:
            tail.next = headA
            break

        if headA.data <= headB.data:
            tail.next = headA
            headA = headA.next
        else:
            tail.next = headB
            headB = headB.next
        tail = tail.next
 
    return dummyNode.next
 
 

listA = LinkedList()
listB = LinkedList()
 
listA.addToList(1)
listA.addToList(2)
listA.addToList(3)
 
listB.addToList(4)
listB.addToList(5)
listB.addToList(6)
 
listA.head = mergeLists(listA.head, listB.head)
 
listA.printList()