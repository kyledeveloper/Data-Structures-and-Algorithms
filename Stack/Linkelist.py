class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
    def setNext(self,newNode):
        self.next = newNode
    
    def getdata(self):
        return self.data

class Linkedlist:
    def __init__(self) -> None:
        self.head = None
        self.count = 0

    def insert(self,newNode, index = 1):
        if self.count == 0:
            self.head = newNode
            self.count +=1
            return
        if index == 1 :
            self.count +=1
            temp = self.head
            self.head = newNode
            self.head.setNext(temp)
            return
        if index == -1:
            currentNode = self.head
            while currentNode.next != None:
                currentNode = currentNode.next
            currentNode.setNext(newNode)

    def delete(self, index = 1):
        if index == 1:
            temp = self.head
            self.head = self.head.next
            self.count -=1
            return temp
    
    def printNodeinList(self):
        currentNode = self.head
        while currentNode != None:
            print(currentNode.data)
            currentNode = currentNode.next
