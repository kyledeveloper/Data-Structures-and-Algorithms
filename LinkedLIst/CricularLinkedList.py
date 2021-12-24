from LinkedList import Node
from LinkedList import SimpleLinkedlist
class CricularLinkedList(SimpleLinkedlist):
    def __init__(self) -> None:
        super().__init__()
        self.tail = None

    def insertAtBegin(self, data):
        currentNode = super().insertAtBegin(data)
        if self.count == 0:
            currentNode.setNext(currentNode)
            self.tail = self.head
        else:
            self.tail.setNext(self.head)

    def inserAtEnd(self, data):
        currentNode = super().inserAtEnd(data)
        # self.tail = currentNode
        # currentNode.setNext(self.head)
        

    def printNodeinList(self):
        counter = 0
        currentNode = self.head
        while counter < self.count and currentNode != None:
            print(currentNode.getdata())
            currentNode = currentNode.getNext()
            counter += 1
    
if __name__ == '__main__':
    mycl = CricularLinkedList()
    mycl.insertAtBegin("kyle")
    mycl.insertAtBegin("elaine")
    mycl.insertAtBegin("hugo")
    mycl.insertAtBegin("mario")
    mycl.insertAtBegin("ee")
    mycl.inserAtEnd("charles")
    
    mycl.printNodeinList()
    print("----")
    name = mycl.getlast().getdata()
    name1 = mycl.getlast().getNext().getdata()
    print(name)
    print(name1)