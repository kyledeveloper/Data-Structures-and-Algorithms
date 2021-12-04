import random
class Node():
    def __init__(self,data = None) -> None:
        self.data = data
        self.next = None
    

class Linkedlist():  
    def __init__(self):
        self.head = None

    def settemphead(self):
        self.temhead = self.head
        return self.temhead

    def nodecount(self):
        counter = 1
        currentNode = self.head
        while currentNode.head.next!= None:
            counter += 1
            currentNode.head = currentNode.head.next
        return counter

    def addNodeAtEnd(self):
        temp = self.settemphead()
        randomnum = random.randint(1,101)
        addNode = Node(randomnum)
        while self.head.next!=None:
            self.head = self.head.next
        self.head.next = addNode
        self.head = temp

    def addNodeAtBegin(self):
        randomnum = random.randint(1,101)
        addNode = Node(randomnum)
        addNode.next = self.head
        self.head = addNode
        
    def printallNode(self):
        temp = self.settemphead()
        while self.head !=None:
            print(self.head.data)
            self.head = self.head.next
        self.head = temp

    def insert(self,num):
        counter = 1
        while counter != num:


if __name__ == '__main__':
    # grobal 
    mylistlist1 = Linkedlist()
    mylistlist1.head = Node("Elaine")
    mylistlist1.head.next = Node("Kyle")


    mylistlist1.addNodeAtEnd()
    mylistlist1.addNodeAtEnd()
    mylistlist1.addNodeAtEnd()
    mylistlist1.addNodeAtBegin()
    mylistlist1.addNodeAtBegin()
    mylistlist1.addNodeAtBegin()
    mylistlist1.printallNode()
    
    print(f'total elements in linked list are {mylistlist1.nodecount()}')
    