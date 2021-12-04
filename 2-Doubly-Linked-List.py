class Node():
    def __init__(self, data = None) -> None:
        self.head = data
        self.previous = None
        self.next = None
class DoublyLinkedList():
    def __init__(self) -> None:
        self.head = None
    
    def 

if __name__ == '__main__':
    myDoublyLinkedlist = DoublyLinkedList()
    myDoublyLinkedlist.head = Node("Elain")
    myDoublyLinkedlist.head.next = Node("Kyle")