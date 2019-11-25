class Node(object):

    def __init__(self, data, Next=None):
        self.data = data
        if Next == None:
            self.Next_node = None
        else:
            self.Next_node = Next

    def __str__(self):
        return str(self.data)
    
    def getdata(self):
        return self.data
    
    def getNext(self):
        return self.Next_node
    
    def setdata(self, data):
        self.data = data
    
    def setNext(self, Next):
        self.Next_node = Next


class Linkedlist(object):

    def __init__(self, head=None):
        if head is None:
            self.head = self.tail = None
            self.size = 0
        else:
            self.head = head
            tail = self.head
            self.size = 1
            while tail.next != None:
                tail = tail.next
                self.size += 1
            self.tail = tail   

    def showlist(self):
        p = self.head
        while p != None:
            print(p.getdata())
            p = p.getNext()

    def insert(self, data):
        new_node = Node(data)
        new_node.setNext(self.head)
        self.head = new_node
    
    def isEmpty(self):
        if self.size > 0:
            return False
        else:
            return True

    def append(self, data):
        p = Node(data)
        if self.head == None:
            self.head = p
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = p


I = Linkedlist()
I.append('B')
I.insert('A')
I.insert('C')
I.showlist()
I.showlist()






