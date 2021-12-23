from LinkedList import SimpleLinkedlist
from LinkedList import Node

class Dnode(Node):
    def __init__(self, data) -> None:
        super().__init__(data)
        self.prev = None
    
    def getPrev(self):
        return self.prev

    def setPrev(self,newNode):
        self.prev = newNode

class DoublyLinkedlist(SimpleLinkedlist):
    def __init__(self) -> None:
        SimpleLinkedlist.__init__(self)
        self.tail = None


    def insertAtBegin(self,data):
        newNode = Node(data)
        if self.count == 0:
            self.head = newNode
            self.tail = newNode
            self.count += 1
            return
        else:
            temp = self.head
            self.head = newNode
            self.head.setNext(temp)
            return

    def insertAtEnd(self,data):
        newNode = Node(data)
        currentNode = self.tail
        


    def insert(self,data,index = 0):
        newNode = Node(data)
        if self.count == 0:
            self.head = newNode
            self.tail = newNode
            self.count += 1
            return
        else:
            self.count += 1
        if index == 0  :
            temp = self.head
            self.head = newNode
            self.head.setNext(temp)
            return

    def printNodeList(self):
        if reversed == 0:
            currentNode = self.head
            while currentNode != None:
                print(currentNode.getdata())
                currentNode = currentNode.getNext()


if __name__ == '__main__':
    mdl = DoublyLinkedlist()
    mdl.insert("kyle")
    mdl.insert('elain')
    mdl.printNodeinList()