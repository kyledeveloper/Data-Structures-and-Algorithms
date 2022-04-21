import random

class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,data):
        self.data = data
    def setNext(self,next):
        self.next = next

class simplyLinkedList():
    def __init__(self) -> None:
        self.head = None
    def insertAtEnd(self,Node):
        if self.head == None:
            self.head.setNext(Node)
        else:
            currentNode = self.head
            while currentNode.next != None:
                currentNode = currentNode.getNext()
            currentNode.setNext(Node)
    

if __name__ == '__main__':
    newlist = simplyLinkedList()
    ranNum = random.randint(1,100)
    newNode = Node(ranNum)
    newlist.insertAtEnd(newNode)
