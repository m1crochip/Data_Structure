from Node import Node
from Stack import Stack
from Queue import Queue

def getunit(num):
    return (num%10)

def gettenit(num):
    return num%100

def gethunit(num):
    return int(num/100)

def RANGEunit(num):
    if num in range(0,10):
        return 0
    elif num in range(10,20):
        return 1
    elif num in range(20,30):
        return 2
    elif num in range(30,40):
        return 3
    elif num in range(40,50):
        return 4
    elif num in range(50,60):
        return 5
    elif num in range(60,70):
        return 6
    elif num in range(70,80):
        return 7
    elif num in range(80,90):
        return 8
    elif num in range(90,100):
        return 9


class LinkedList:
    def __init__(self, head=None):
        self.head = head
    def size(self):
        p = self.head
        count = 1
        while p.next != None:
            count += 1
            p = p.next
        return count
    def isEmpty(self):
        return self.size() == 0
    def append(self, data):
        if isinstance(data, Node):
            newNode = data
        else:
            newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            p = self.head
            while True:
                if p.next is None:
                    p.next = newNode
                    break
                p = p.next

    def isIn(self, data):
        p = self.head
        found = False
        while p != None:
            if p.data == data:
                found = True
                break
            p = p.next
        return found

    def __str__(self):
        p = self.head
        s = ''
        while p != None:
            s += str(p.data)+' '
            p = p.next
        return "in LinkedList : " + s

    def before(self, data):
        p = self.head
        count = 0
        if self.isIn(data):
            while p.next.data != data:
                count += 1
                p = p.next
            return p
        else:
            print(data," Not Found")

    def getHead(self):
        return self.head

    def getTail(self):
        p = self.head
        while p.next != None:
            p = p.next
        return p

    def addHead(self, data):
        if isinstance(data, Node):
            newNode = data
        else:
            newNode = Node(data)
        newNode.setNext(self.head)
        self.head = newNode

    def removeHead(self):
        p = self.head
        self.head = p.next

    def remove(self, data):
        p = self.head
        if p is data:
            self.removeHead()
        elif self.isIn(data):
            prev = self.head
            current = prev.next
            while current.data != data:
                prev = prev.next
                current = current.next
            prev.setNext(current.next)
            current.setNext()

        return current

    def sortunit(self):
        Length = self.size()
        temp = []
        sort = [[],[],[],[],[],[],[],[],[],[]]
        p = self.head
        while p != None:
            temp.append(p.getData())
            p = p.next
        for i in range(0,Length):
            sort[getunit(temp[i])] = temp[i]
        #print(sort)
        unit100 = [[], [], [], [], [], [], [], [], [], []]
        for i in range(0,Length):
            unit100[RANGEunit(gettenit(sort[i]))].append(sort[i])
        UNIT = []
        for i in range(0,Length):
            UNIT.extend(unit100[i])
        Qu = [[], [], [], [], [], [], [], [], [], []]
        for i in range(0,Length):
            Qu[gethunit(UNIT[i])].append(UNIT[i])
        OUTPUT = []
        for i in range(0,Length):
            OUTPUT.extend(Qu[i])
        return OUTPUT
    
      

