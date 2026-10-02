class Node:
    def __init__(self, info, next=None):
        self.data = info
        self.next = next

class CircularLL:
    def __init__(self, head = None):
        self.head = head

    def insertAtEnd(self, value):
        temp = Node(value)
        if(self.head != None):
            t1 = self.head
            while t1.next != None:
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp

    def insertAtBeg(self,value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp

    def insertAtMid(self, value, x): # x -> existing value after which the new value will be inserted
        temp = Node(value)
        t1 = self.head
        while(t1.next != None):
            if(t1.data == x):
                temp.next = t1.next
                t1.next = temp
            t1 = t1.next

    def deleteLinkedList(self, value):
        t1 = self.head
        prev = t1
        if(self.head.data == value):
            self.head = t1.next
        while(t1.next != None):
            if(t1.data == value):
                prev.next = t1.next
                return
            else:
                prev = t1
                t1 = t1.next
        if(t1.data == value):
            prev.next = None

    def printLinkedList(self):
            t1 = self.head
            while t1.next != None:
                print(t1.data)
                t1 = t1.next
            print(t1.data)

obj = CircularLL()
obj.insertAtEnd(10)
obj.insertAtEnd(100)
obj.insertAtEnd(10000)

obj.printLinkedList()
print()

obj.insertAtBeg(1)

obj.printLinkedList()
print()

obj.insertAtMid(1000, 100)
obj.printLinkedList()
print()

obj.deleteLinkedList(100)
obj.printLinkedList()
print()

obj.deleteLinkedList(1)
obj.printLinkedList()
print()