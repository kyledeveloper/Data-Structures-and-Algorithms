def isNode(data):
    if type(data) == Node:
        return True
    else:
        return False

class Node():
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
    
    def __str__(self) -> str:
        if self.next == None:
            return f'CurrentNode: {self.data}----> End'
        if self.next != None:
            return f'CurrentNode: {self.data}----> NextNode: {self.next.data}'
class SimpleLinkedList ():
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def createNode(self,data):
        newNode = Node(data)
        return newNode

    # def createNode(self):
    #     randomNum = random.randint(0,101)
    #     newNode = Node(randomNum)
    #     return newNode
        
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False

    def addInBegin(self,data):
        newNode = SimpleLinkedList.createNode(self, data)
        if SimpleLinkedList.isEmpty(self):
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def addInEnd(self, data):
        newNode = SimpleLinkedList.createNode(self, data)
        if SimpleLinkedList.isEmpty(self):
            self.head = newNode
            self.tail = newNode
        else:
            currentNode = self.tail
            self.tail = newNode
            currentNode.next = newNode

    def printNodeInList(self):
        currentNode = self.head
        print(currentNode)
        while currentNode.next != None:
            currentNode = currentNode.next
            print(currentNode)


    def reverse(self):
        copyList = self
        newlist = SimpleLinkedList()
        currentNode = copyList.head
        while  currentNode.next != None :
            while currentNode.next != None:
                previous  = currentNode
                currentNode = currentNode.next
            newlist.addInEnd(currentNode.data)
            previous.next = None         
            currentNode = copyList.head
        newlist.addInEnd(copyList.head.data)
        return newlist
    
    def foundNode(self,data):
        isfound = False
        currentNode = self.head
        while currentNode.next != None :
            if currentNode.data == data:
                print(f'Found it : {currentNode}')
                isfound =True
                break
            else:
                currentNode = currentNode.next
        if  not isfound:
            print(f"{data} not found")
            return None
        else :
            return currentNode
            


        

if __name__ == "__main__":
    newList = SimpleLinkedList()
    newList.addInBegin("Kyle")
    newList.addInEnd("Elaine")
    newList.addInBegin('ee')
    newList.addInBegin("kk")
    newList.printNodeInList()
    newList.foundNode('jask')
    newList.reverse().printNodeInList()

