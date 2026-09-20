class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

class SinglyLL:
    def __init__(self, head = None):
        self.head = head

    def insertAtBeg(self, data):
        temp = Node(data)
        if self.head == None:
            self.head = temp
        else:
            temp.next = self.head
            self.head = temp

    def insertAtMid(self, data, elem):
        temp = Node(data)
        t = self.head
        if t == None:
            t = temp
        else:
            while t.next != None:
                if elem == t.data:
                    temp.next = t.next
                    t.next = temp
                t = t.next

    def insertAtEnd(self, data):
        temp = Node(data)
        if self.head == None:
            self.head = temp
        else: 
            t = self.head
            while t.next != None:
                t = t.next
            t.next = temp

    def printLL(self):
        if self.head == None:
            return
        else: 
            t = self.head
            while t.next != None:
                print(t.data)
                t = t.next
            print(t.data)

    def deleteNode(self, element):
        t = self.head
        prev = t
        if t.data == element:
            self.head = t.next

        while t.next != None:
            if t.data == element:
                prev.next = t.next
                return 
            else:
                prev = t
                t = t.next

        if t.data == element:
            prev.next = None


ll = SinglyLL()

ll.insertAtBeg(30)
ll.insertAtBeg(25)
ll.insertAtEnd(35)
ll.insertAtEnd(50)
ll.insertAtMid(45, 35)
ll.insertAtMid(40, 35)

ll.printLL()

ll.deleteNode(30)
ll.deleteNode(25)
ll.deleteNode(50)

print()
ll.printLL()