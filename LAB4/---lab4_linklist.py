class Node:
    def __init__(self, data, Next=None):
        self.data = data
        self.next = Next
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self, data):
        self.data = data
    def setNext(self, Next):
        self.next = Next
    


class LinkedList:
    def __init__(self, head=None):
        self.head = head
    def append(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.getNext
        cur.setNext(new_node)
    def size(self):
        cur = self.head
        count = 0
        while cur.getNext() != None:
            count+=1
            cur = cur.getNext()
        return count
    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.getNext != None:
            cur_node = cur_node.getNext()
            elems.append(cur_node.getData())
        print(elems) 


mylist = LinkedList()
mylist.append('1')
mylist.display()