class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.previous = None
        self.next = None

    def __str__(self) -> str:
        if self.previous == None and self.next == None:
            return (
                f"Previous Node: None <---Current Node: {self.data}--->Next Node: None"
            )
        elif self.next == None:
            return f"Previous Node: {self.previous.data}<---Current Node: {self.data}--->Next Node: Tail"
        elif self.previous == None:
            return f"Previous Node: Beginning <---Current Node: {self.data}--->Next Node: {self.next.data}"
        return f"Previous Node: {self.previous.data}<---Current Node: {self.data}--->Next Node: {self.next.data}"


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.count = 0

    def create_a_Node(self, data):
        self.count += 1
        if self.head == None:
            newNode = Node(data)
            self.head = newNode
            self.tail = newNode
        else:
            newNode = Node(data)
            return newNode

    def add_at_begin(self, data):
        currentNode = self.head
        newNode = DoublyLinkedList.create_a_Node(self, data)
        currentNode.previous = newNode
        newNode.next = currentNode
        self.head = newNode

    def add_at_end(self, data):
        currentNode = self.tail
        newNode = DoublyLinkedList.create_a_Node(self, data)
        currentNode.next = newNode
        newNode.previous = currentNode
        self.tail = newNode

    def insert_in_middle(self, data, num):
        index = 1
        currentNode = self.head
        while index < num:
            currentNode = currentNode.next
            index += 1
        nextNode = currentNode.next
        newNode = DoublyLinkedList.create_a_Node(self, data)
        newNode.previous = currentNode
        newNode.next = currentNode.next
        nextNode.previous = newNode
        currentNode.next = newNode

    def print_node_in_list(self):
        currentNode = self.head
        while currentNode.next != None:
            print(currentNode)
            currentNode = currentNode.next
        print(currentNode)

    def delNode(self, num):
        if num == 1:
            currentNode = self.head
            currentNode.next.previous = None
            self.head = currentNode.next
        elif num == -1:
            currentNode = self.tail
            currentNode.previous.next = None
            self.tail = currentNode.previous
        else:
            index = 1
            currentNode = self.head
            while index < num:
                currentNode = currentNode.next
                index += 1
            connectnext = currentNode.previous
            connectprevious = currentNode.next
            connectnext.next = connectprevious
            connectprevious.previous = connectnext
        self.count -= 1


if __name__ == "__main__":
    myDoublyLinkedlist = DoublyLinkedList()
    myDoublyLinkedlist.create_a_Node("Elaine")
    myDoublyLinkedlist.add_at_end("Kyle")
    myDoublyLinkedlist.add_at_end("Ming")
    myDoublyLinkedlist.add_at_begin("Meimei")
    myDoublyLinkedlist.add_at_begin("Jenny")
    myDoublyLinkedlist.insert_in_middle("Kerwin", 2)
    myDoublyLinkedlist.delNode(2)
    myDoublyLinkedlist.print_node_in_list()
    print(myDoublyLinkedlist.count)
    # initcialNode = Node("Elaine")
    # initcialNode2 = Node("Kyle")
    # initcialNode3 = Node('2')

    # myDoublyLinkedlist.head = initcialNode
    # initcialNode.next = initcialNode2
    # initcialNode2.previous = initcialNode
    # initcialNode3.previous = initcialNode2
    # initcialNode2.next = initcialNode3
    # print(initcialNode2)
    # print(initcialNode)
    # print(initcialNode3)
