class Node:
    def __init__(self, data = None):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLL:
    def __init__(self):
        self.head = None

    def insertAtEnd(self, data):
        temp = Node(data)
        if self.head == None:
            self.head = temp
            return
        t = self.head
        while t.next != None:
            t = t.next
        # Reached at the end
        t.next = temp
        temp.prev = t

    def insertAtBeg(self, data):
        temp = Node(data)
        if self.head == None:
            self.head = temp
        else:
            temp.next = self.head
            self.head.prev = temp
            self.head = temp

    def insertAtMid(self, data, elem):
        temp = Node(data)
        t = self.head
        while t.next != None:
            if t.data == elem:
                # found element after which new Node to be inserted
                temp.next = t.next
                t.next = temp
                temp.prev = t
                temp.next.prev = temp
                return
            else:
                t = t.next
        self.insertAtEnd(data)

    def deleteNode(self, elem):
        if self.head == None:
            print("Linked list is empty")

        t = self.head
        if t.data == elem:
            self.head = t.next
            self.head.prev = None
            return
        while t.next != None:
            if t.data == elem:
                t.prev.next = t.next
                t.next.prev = t.prev
                return
            else:
                t = t.next
        if t.data == elem:
            t.prev.next = None
            t.prev = None
                        

    def printLL(self):
        t = self.head
        while t.next != None:
            print(t.data, end=" <--> ")
            t = t.next
        print(t.data)


obj = DoublyLL()
obj.insertAtEnd(10)
obj.insertAtEnd(100)
obj.insertAtEnd(1000)
obj.insertAtEnd(10000)


obj.insertAtMid(15, 10)
obj.insertAtMid(150, 100)

obj.insertAtBeg(1)

obj.printLL()

obj.deleteNode(15)
obj.deleteNode(10000)

obj.printLL()